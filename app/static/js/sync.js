window.fileSync = (function (w) {

  var api = {}
    , dir
    , root;

  // set up event handlers and file system
  api.init = function (fs) {

    dir = document.getElementById('dir-tree');
    dir.addEventListener('click', api.fileAction, false);

    root = fs.root;

    // offline detection
    w.addEventListener("offline", api.toggleOnlineState, false);
    w.addEventListener("online", api.refreshFiles, false);

    if (w.navigator.onLine) {

        setInterval(function() {
        $.get('http://project-livec9fd0cdb8477.rhcloud.com/check', function(data) {
            newData = JSON.parse(data);
            var contents = newData['contents'];
            console.log(contents);
            var table = $("#listing")
            table.html = ""
            table.html += "<tr><td><b>Filename</b></td><td><b>Size (bytes)</b></td><td><b>Date modified</b></td><td><b>&nbsp;</b></td></tr>"
            for(var i = 0; i < contents.length; i++) {
                table.html += "<tr><td>" + contents[i]['path'] + "</td><td>" + contents[i]['bytes'] + "</td><td>" +  contents[i]['modified'] + "</td><td><a class='downloader' id='" + data[i]['filename'] + "'>Download</a></td></tr>"
            }
            console.log('done...?')
        })},50000);

    }

    api.toggleOnlineState();
    api.syncStatus();

  };


  api.syncStatus = function () {

    var dr = root.createReader();
    dr.readEntries(api.updateStatus, api.err);
    api.toggleOnlineState();

  };


  api.toggleOnlineState = function () {

    var i = 0
      , d = 'none'
      , sy = dir.querySelectorAll(".sync");

    if (w.navigator.onLine) {
      d = 'inline-block';
    }

    for (i = 0; i < sy.length; ++i) {
      sy.item(i).style.display = d;
    }

  };

  //event handler for tree node actions
  api.fileAction = function (ev) {

    var t = ev.target, name;

    if (t.nodeName.toLowerCase() === 'a') {

      name = t.href.match(/[^/]+$/)[0];

      if (t.className.indexOf('sync') !== -1) {

        t.parentNode.parentNode.className = 'file-entry syncing';
        api.pull(t.href, name);

      }

      else if (t.className.indexOf('open') !== -1) {

        if (t.className.indexOf('synced') === -1) {
          api.pull(t.href, name, true);
        }

        else {
          api.open(name);
        }

      }

      ev.preventDefault();

    }

  };


  // pull file down into local
  api.pull = function (url, name, open) {

    var xhr = new XMLHttpRequest;

    xhr.open('get', url, true);
    xhr.responseType = 'arraybuffer';
    xhr.onload = function () {

      var res = this.response;

      root.getFile(name, {create: true}, function (fe) {

        fe.createWriter(function(writer) {

          var bb = new w.WebKitBlobBuilder;

          writer.onwriteend = function () {
            
            api.flagSynced(fe);

            if (open) {
              api.open(name);
            }

          }
          writer.onerror = api.err;

          bb.append(res);
          writer.write(bb.getBlob());

        });

      }, api.err);

    }

    xhr.send();

  };


  api.open = function (name) {

    if (typeof name === 'string') {

      root.getFile(name, {}, function (fe) {

        w.location = fe.toURL();

      }, api.err);

    }

    else {
      w.location = name.toURL();
    }

  };
  // default error handler - that doesn't do anything useful
  api.err = function (ev) {
    console.log(ev);
  };

  return api;

})(window);

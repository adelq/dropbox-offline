<!doctype html>
<html manifest="sync.appcache">
  <head>
    <title>Offline files with HTML5</title>
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>

    <div id="no-support">
      Your browser doesn't support this demo, you'll need to
      grab the latest version of <a href="http://www.google.co.uk/chrome">
      Google Chrome</a> to be sure it will work.
    </div>

    <ol id="dir-tree">

      <?php include 'file-list.php'; ?>

    </ol>

  </body>
  <script src="js/sync.js"></script>
  <script>

    (function (w) {

      if (typeof w.webkitRequestFileSystem === 'undefined') {

        document.getElemntById('no-support').style.display = 'block';
        return;
        
      }

      w.webkitStorageInfo.requestQuota(w.PERSISTENT, 5*1024*1024, function(gb) {
        w.webkitRequestFileSystem(
            w.PERSISTENT
          , gb
          , fileSync.init
          , fileSync.err
        );
      }, fileSync.err);

    })(window);

  </script>
</html>

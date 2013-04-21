var client = new Dropbox.Client({
	// set up the API key for oauth
	key: 'uEVRWTeOF6A=|WWQHgrqEN60JX7T924IWhNMjcKqTarBW+f0v4PiVoA==', sandbox: true // encoded key
});

client.authDriver(new Dropbox.Drivers.Chrome({
	// set up an auth driver that redirects the user to the auth screen
	// after successful auth the user is redirected again, this time to 'receiver.html'
	receiverPath: 'receiver.html'
}));

client.authenticate(function(error, successClient) {
	// authenticate the client using the auth driver
	if(error) {
		return console.log(error);
	}
	
	var apiClient = successClient;
	// apiClient will be used to send API calls
});

function fetchFileFromDropbox(filename) {
	apiClient.readFile('test.file', function(error, data) {
		if(error) {
			return console.log(error);
		}
	
		fs.root.getFile(filename), {create:true, exclusive:true}, function(fileObject) {
			return console.log('file with name ' + filename + 'written to filesystem...');
		}, function(error) {
			console.log(error);
		});
	});
}

// this part might be buggy because background processes might not have a window object

window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;

window.webkitStorageInfo.requestQuota(PERSISTENT, 4096*4096, function(grantedBytes) {
	window.requestFileSystem(window.PERSISTENT, 4096, function(fileSystem) {
		return console.log('filesystem initialized?');
	}, function(fileError) {
		return console.log(error);
	});
});

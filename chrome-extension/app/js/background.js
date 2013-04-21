var client = new Dropbox.Client({
	key: 'uEVRWTeOF6A=|WWQHgrqEN60JX7T924IWhNMjcKqTarBW+f0v4PiVoA==', sandbox: true // encoded key
});

client.authDriver(new Dropbox.Drivers.Chrome({
	receiverPath: 'reciever.html'
}));

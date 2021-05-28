const redis = require('redis');
const client = redis.createClient();
const channels = ['holberton school channel'];

client.on('connect', () => {
    console.log("Redis client connected to the server")
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit();
    }
});

client.subscribe(...channels);

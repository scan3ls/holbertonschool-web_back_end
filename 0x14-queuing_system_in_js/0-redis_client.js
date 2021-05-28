const redis = require('redis');

const client = redis.createClient();

client.on('ready', function(){
    console.log('Redis client connected to the server');
});

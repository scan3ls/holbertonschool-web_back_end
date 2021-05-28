const redis = require('redis');
const client =  redis.createClient();

const hash = 'HolbertonSchools'
const pairs =  {
    "Portland": "50",
    "Seattle": "80",
    "New York": "20",
    "Bogota": "20",
    "Cali": "40",
    "Paris": "2",
}

client.on('ready', () => {
    console.log('Redis client connected to the server');
});

for (const key in pairs) {
    const value = pairs[key];
    client.hset(hash, key, value, redis.print);
}

client.hgetall(hash, (key, value) => {
    console.log(value);
});

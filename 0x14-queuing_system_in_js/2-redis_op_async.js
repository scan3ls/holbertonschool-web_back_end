const redis = require('redis');
const { promisify } = require("util");
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
  if (err)
    console.log(`Redis client not connected to the server: ${err}`);
});

client.on('ready', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value);
}

(async() => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();

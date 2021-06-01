const kue = require('kue');
const queue = kue.createQueue();

const job = queue.create(
    'push_notification_code',
    {
        phoneNumber: '1234567890',
        message: 'string',
    }
).save( (err) => {
    if (err) console.log(err.message);
    else console.log(`Notification job created: ${job.id}`);
});

queue.on('complete', () => {
    console.log('Notification job completed');
});

queue.on('failing', () => {
    console.log('Notification job failed');
});

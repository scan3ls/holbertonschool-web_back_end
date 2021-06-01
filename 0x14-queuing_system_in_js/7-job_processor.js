const kue = require('kue');
const queue = kue.createQueue();

const blacklist = [
    '4153518780',
    '4153518781',
];

function sendNotification(phoneNumber, message, job, done) {

    if (blacklist.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    const next = (progress) => {
        job.progress(progress, 100);
        if (progress >= 50) {
            console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
            done();
        } else {
            next(progress + 50);
        }
    };

    next(0);
}

queue.process(
    'push_notification_code_2',
    2,
    (job, done) => {
        sendNotification(job.data.phoneNumber, job.data.message, job, done);
        done();
    }
);

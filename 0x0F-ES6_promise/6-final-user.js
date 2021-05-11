import signUpUser from "./4-user-promise.js"
import uploadPhoto from "./5-photo-reject.js"

function handleProfileSignup(firstName, lastName, fileName) {

    const res1 = signUpUser(firstName, lastName).catch();
    const res2 = uploadPhoto(fileName).catch();

    return Promise.all([res1, res2])
    .finally((values) => value).catch(() => {});
}

export default handleProfileSignup;

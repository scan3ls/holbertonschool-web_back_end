import {uploadPhoto, createUser} from "./utils.js"

function handleProfileSignup() {
    Promise.all([createUser(), uploadPhoto()])
    .then((responses) => {
        const res_user = responses[0];
        const res_photo = responses[1];

        const res_str = `${res_photo.body} ${res_user.firstName} ${res_user.lastName}`
        console.log(res_str);

    }, () => {
        console.log("Signup system offline");
    });
}

export default handleProfileSignup;

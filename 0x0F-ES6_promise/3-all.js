import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([createUser(), uploadPhoto()])
    .then((responses) => {
      const resUser = responses[0];
      const resPhoto = responses[1];

      const resStr = `${resPhoto.body} ${resUser.firstName} ${resUser.lastName}`;
      console.log(resStr);
    }, () => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;

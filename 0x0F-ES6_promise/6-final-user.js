import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  const res1 = signUpUser(firstName, lastName);
  const res2 = uploadPhoto(fileName);

  return Promise.allSettled([res1, res2]).then(
    (thing) => {
      for (const obj of thing) {
        const value = obj.reason;
        if (value !== undefined) {
          delete obj.reason;
          obj.value = value.toString();
        }
      }
      return thing;
    },
  );
}

export default handleProfileSignup;

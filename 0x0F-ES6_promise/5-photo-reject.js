function uploadPhoto(fileName) {
    const msg = `${fileName} cannot be processed`
    return Promise.reject(new Error(msg)).catch(() => {});
}

export default uploadPhoto;

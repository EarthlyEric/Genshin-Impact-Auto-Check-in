function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }
var ltuid=getCookie('ltuid');
var ltoken=getCookie('ltoken');
console.log('ltuid:');
console.log(ltuid);
console.log('ltoken:');
console.log(ltoken);
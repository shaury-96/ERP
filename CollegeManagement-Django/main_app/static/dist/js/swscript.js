const checkPermission = () =>{
    if(!('serviceWorker' in navigator))
    {
        throw new Error("No support for service worker");
    }
    if(!('Notification' in window))
    {
        throw new Error("NO support for notification app");
    }
}

const registerSW = async()=>{
    const registration=await navigator.serviceWorker.register('/static/dist/js/ssw.js');
    return registration;
}

const requestNotificationPermission = async()=>{
    const permission= await Notification.requestPermission();
    if(permission !== 'granted')
        throw new Error("Notification permission not granted");
   
}

const main = async() =>{
    checkPermission();
    await requestNotificationPermission();
    await registerSW();  
   
}

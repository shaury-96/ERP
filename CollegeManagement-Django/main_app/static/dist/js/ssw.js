function urlB64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/');

    const rawData = atob(base64);
    const outputArray = new Uint8Array(rawData.length);
    
    for(let i=0;i<rawData.length;++i)
        outputArray[i]=rawData.charCodeAt(i);

    return outputArray;
}
const saveSubscription = async(subscription) =>{
    const response = await fetch('/webpush/save_information/',{
        method:'post',
        headers:{'Content-type':"application/json"},
        body: JSON.stringify(subscription)
    })
    return response.json()
}
self.addEventListener("activate", async(e)=>{
    const subscription = await self.registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlB64ToUint8Array("BKu-pT0gEj0Xdr4tzJe1oisdaa8ZapnuObYc5jtQR9olLUDAoGX3YtoahoA7_jjSTwX__DFsLSLtLmFwsui9SP4")
    })
    
    console.log(subscription);
    const response= await saveSubscription(subscription);
    console.log(response);
})

self.addEventListener("push",event=>{
    
    let data = {};
    
    if (event.data) {
        data = event.data.json();  
    }

    const options = {
        body: data.body || 'Default body text',  
        icon: data.icon || '/static/default_icon.png', 
        data: {  
            url: data.url || 'http://127.0.0.1:8000'
        }
    };

    event.waitUntil(
        self.registration.showNotification(data.head || 'Default Title', options)
    );
})

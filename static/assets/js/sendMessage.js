function SendMessageFun(event) {
    // event.preventDefault();
    // if(   document.querySelector('.sendMessageName').value == ''  ||   document.querySelector('.sendMessageAge').value == ''  ||   document.querySelector('.sendMessageCouse').value == ''  ||   document.querySelector('.sendMessagePhone').value == ''  ||   document.querySelector('.sendMessageMotherFatherPhone').value == ''  ||   document.querySelector('.sendMessageLocation').value == ''){
    //     return false
    // } else {
    let name = document.querySelector('.sendMessageName').value;

    let age = document.querySelector('.sendMessageAge').value;

    let course = document.querySelector('.sendMessageCouse').value;

    let phoneNumber = document.querySelector('.sendMessagePhone').value;

    let motherFatherPhoneNumber = document.querySelector('.sendMessageMotherFatherPhone').value;

    let location = document.querySelector('.sendMessageLocation').value;

    let Message = `Yangi o'quvchi 
    %0A - Ismi : ${name} 
    %0A - Yoshi : ${age} 
    %0A - Tanlangan kurs nomi : ${course} 
    %0A - Telefon raqami : ${phoneNumber}
    %0A - Ota-onasining telefon raqami : ${motherFatherPhoneNumber}
    %0A - Yashash manzili : ${location}`

    const token = "5732088664:AAFacCa41VSKpDiack1RWBDD_PhFBEuiJd0";
    const chat_id = -1001891141082;
    const url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${Message}/`;

    let api = new XMLHttpRequest();
    api.open("GET" , url , true)
    api.send();

    // return true
    // }

}



function sendNumberFun(){
    if(
        document.querySelector('.footerGetNumber').value == ''
    ) {
        return false
    }
    else {
        let phoneNumber = document.querySelector('.footerGetNumber').value;
        let Message = `Yangi o'quvchi 
        %0A - Telefon raqami : +998${phoneNumber}`
    
        const token = "5543406354:AAHVuB3iXpE1KSRm59ksyIwxuiWnayjqKIs";
        const chat_id = -1001861892006;
        const url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${Message}/`;
    
        let api = new XMLHttpRequest();
        api.open("GET" , url , true)
        api.send();
        return true
    }
}
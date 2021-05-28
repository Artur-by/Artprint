function getSumBySex(sum) {
    let sex = document.getElementById('id_Пол')
    if (sex.value == 1){
        sum += 0
    }
    else if (sex.value == 2){
        sum += 0.5
    }
    else if (sex.value == 3){
        sum += 0
    }

    return sum
}

function getSumBySize(sum){
    let size = document.getElementById('id_Размер принта')
    if (size.value == 1){
        sum += 0
    }
    else if (size.value == 2){
        sum += 1
    }
    else{
        sum += 2
    }
    return sum
}

function getSumByPrint(sum) {
    let format = document.getElementById('id_Формат')
    if (format.value == 1){
        sum += 5
    }
    else {
        sum += 7
    }
    return sum
}

function costValue(){
    let sum = 20
    sum = getSumBySex(sum)
    sum = getSumBySize(sum)
    sum = getSumByPrint(sum)

    let output = document.getElementById('costValueText')
    output.innerHTML = ' Цена '+ sum + ' руб.'
}

function zamena(element){
    let a = document.getElementById('imgValue')
    if(element.id == "img1") {
        a.src="/static/image/tolst2.png";
    }
    else if(element.id == "img2"){
        a.src="/static/image/tolst1.png";
    }
    else if(element.id == "img3"){
        a.src="/static/image/tolst3.png";
    }
    else if(element.id == "img4"){
        a.src="/static/image/tolst4.png";
    }
    else if(element.id == "img5"){
        a.src="/static/image/tolst5.png";
    }
    else if(element.id == "img6"){
        a.src="/static/image/tolst6.png";
    }
}
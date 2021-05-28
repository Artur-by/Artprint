function getSumByCant(sum) {
    let cant = document.getElementById('id_Кант')
    if (cant.value == 1){
        sum += 0
    }
    else if (cant.value == 2){
        sum += 0.5
    }
    return sum
}


function getSumByPrint(sum) {
    let format = document.getElementById('id_Формат')
    if (format.value == 1){
        sum += 1
    }
    else if (format.value == 2){
        sum += 2
    }
    else {
        sum += 3
    }
    return sum
}

function costValue(){
    let sum = 7
    sum = getSumByCant(sum)
    sum = getSumByPrint(sum)

    let output = document.getElementById('costValueText')
    output.innerHTML = ' Цена '+ sum + ' руб.'
}
function zamena(element){
    let a = document.getElementById('imgValue')
    if(element.id == "img1") {
        a.src="/static/image/apron1.png";
    }
    else if(element.id == "img2"){
        a.src="/static/image/apron2.png";
    }
    else if(element.id == "img3"){
        a.src="/static/image/apron3.png";
    }
    else if(element.id == "img4"){
        a.src="/static/image/apron4.png";
    }
    else if(element.id == "img5"){
        a.src="/static/image/apron5.png";
    }
    else if(element.id == "img6"){
        a.src="/static/image/apron6.png";
    }
}

function getSumByColor(sum) {
    let color = document.getElementById('id_Цвет')
    if (color.value == 1){
        sum += 0
    }
    else if (color.value == 2){
        sum += 0.5
    }
    else if (color.value == 3){
        sum += 0
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
    let sum = 6
    sum = getSumByColor(sum)
    sum = getSumByPrint(sum)

    let output = document.getElementById('costValueText')
    output.innerHTML = ' Цена '+ sum + ' руб.'
}

function zamena(element){
    let a = document.getElementById('imgValue')
    if(element.id == "img1") {
        a.src="/static/image/shopper1-1.png";
    }
    else if(element.id == "img2"){
        a.src="/static/image/shopper1-2.png";
    }
    else if(element.id == "img3"){
        a.src="/static/image/shoper1-3.png";
    }
    else if(element.id == "img4"){
        a.src="/static/image/shoper1-4.png";
    }
    else if(element.id == "img5"){
        a.src="/static/image/shoper1-5.png";
    }
    else if(element.id == "img6"){
        a.src="/static/image/shoper1-6.png";
    }
}



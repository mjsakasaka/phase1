document.getElementById("burger").addEventListener("click", function() {
    document.getElementById("popup-menu").style.display = "block";
});

document.getElementById("close-btn").addEventListener("click", function() {
    document.getElementById("popup-menu").style.display = "none";
});

function parseImg(Arr, n, m){
    for (let i = 1; i <= m; i++){
        let box = document.querySelector("#box_" + (i+n).toString());
        // 图片部分
        let imgUrls = Arr[i+n+2].filelist.toLowerCase();
        let imgUrl = imgUrls.split("jpg")[0] + "jpg";
        let bigboxImg = document.querySelector("#bigboximg"+ (i+n).toString());
        bigboxImg.src = imgUrl;
        // 文字部分
        let newDiv = document.createElement("div");
        newDiv.className = "bigboxtext";
        newDiv.id = "bigboxtext" + (i+n).toString();
        box.appendChild(newDiv);
        newDiv = document.querySelector("#bigboxtext" + (i+n).toString());
        let innerDiv = document.createElement("div");
        innerDiv.textContent = Arr[i+n+2].stitle;
        innerDiv.className = "bigboxinnertext";
        newDiv.appendChild(innerDiv);
    }
};

let n = 0; // 用于loadmore
let m = 10; // 用于parse几张图片

fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
.then(function(response){
    return response.json();
})
.then(function (spotData){
    let spotArr = spotData.data.results;
    // 处理三个small box
    for (let i = 1; i < 4; i++){
        let box = document.querySelector("#smallbox_" + i.toString());
        // 图片部分
        let imgUrls = spotArr[i-1].filelist.toLowerCase();
        let imgUrl = imgUrls.split("jpg")[0] + "jpg";
        let newImg = document.createElement("img");
        newImg.src = imgUrl;
        newImg.className = "smallboximg";
        box.appendChild(newImg);
        // 文字部分
        let newDiv = document.createElement("div");
        newDiv.textContent = spotArr[i-1].stitle;
        box.appendChild(newDiv);
    }
    // 处理10个bigbox
    parseImg(spotArr, n, m);
});

function loadmore(){
    n += 10;
    if (n == 50){
        m = 5;
    };
    if (n > 40){
        document.querySelector("#loadmore").style.display = "none";
    }
    for (let i = 1; i <= m; i++){
        // 外层bigbox
        let mainBottom = document.querySelector("#mainbottom");
        let bigBox = document.createElement("div");
        if (i % 5 == 1){
            bigBox.className = "bigbox_1";
        } else {
            bigBox.className = "bigbox";
        }
        bigBox.id = "box_" + (i+n).toString();
        mainBottom.appendChild(bigBox);
        // 内层bigboximg
        let bigBoxImg = document.createElement("img");
        bigBoxImg.className = "bigboximg";
        bigBoxImg.id = "bigboximg" + (i+n).toString();
        bigBox.appendChild(bigBoxImg);
        // 内层starline
        let starLine = document.createElement("div");
        starLine.className = "starline"
        bigBox.appendChild(starLine);
        // starline内层img
        let star = document.createElement("img");
        star.src = "star_icon.png";
        star.className = "star";
        starLine.appendChild(star);
    }
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
    .then(function(response){
        return response.json();
    })
    .then(function (spotData){
        let spotArr = spotData.data.results;
        parseImg(spotArr, n, m);
    });
};

document.getElementById("burger").addEventListener("click", function() {
    document.getElementById("popup-menu").style.display = "block";
});

document.getElementById("close-btn").addEventListener("click", function() {
    document.getElementById("popup-menu").style.display = "none";
});

fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
.then(function(response){
    return response.json();
})
.then(function(spotData){
    let spotArr = spotData.data.results;
    // 处理三个small box
    for (let i = 1; i < 4; i++){
        let box = document.querySelector("#box_" + i.toString());
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
    for (let i = 4; i < 14; i++){
        let box = document.querySelector("#box_" + i.toString());
        // 图片部分
        let imgUrls = spotArr[i-1].filelist.toLowerCase();
        let imgUrl = imgUrls.split("jpg")[0] + "jpg";
        let bigboxImg = document.querySelector("#bigboximg"+ i.toString());
        bigboxImg.src = imgUrl;
        // 文字部分
        let newDiv = document.createElement("div");
        newDiv.className = "bigboxtext";
        newDiv.id = "bigboxtext" + i.toString();
        box.appendChild(newDiv);
        newDiv = document.querySelector("#bigboxtext" + i.toString());
        let innerDiv = document.createElement("div");
        innerDiv.textContent = spotArr[i-1].stitle;
        innerDiv.className = "bigboxinnertext";
        newDiv.appendChild(innerDiv);
    }
});

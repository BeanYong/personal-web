/**
 * 图片链接数组
 */
var imgSrcArr = [
	"http://120.79.198.228/personal-site/imgs/nanchang01.jpg",
	"http://120.79.198.228/personal-site/imgs/nanchang02.jpg",
	"http://120.79.198.228/personal-site/imgs/shanghai01.jpg",
	"http://120.79.198.228/personal-site/imgs/shanghai02.jpg",
	"http://120.79.198.228/personal-site/imgs/shanghai03.jpg",
	"http://120.79.198.228/personal-site/imgs/shinian01.jpg",
	"http://120.79.198.228/personal-site/imgs/tianshui01.jpg",
	"http://120.79.198.228/personal-site/imgs/wechat.jpg",
	"http://120.79.198.228/personal-site/imgs/yangzhou01.jpg",
	"http://120.79.198.228/personal-site/imgs/yangzhou02.jpg",
	"http://120.79.198.228/personal-site/imgs/zhenjiang01.jpg",
	"http://120.79.198.228/personal-site/imgs/zhenjiang02.jpg",
	"http://120.79.198.228/personal-site/imgs/zhenjiang03.jpg"
];

var hasLoadedCount = 0;//已经加载完毕的图片计数
var imgSrcArrLen = imgSrcArr.length;//图片数组长度

/**
 * 预加载图片
 * 
 * @param imgSrcArr 图片链接数组
 */
var preloadImages = function(imgSrcArr){
	$.each(imgSrcArr, function(index, imgSrc){
        var imgObj = new Image();
        $(imgObj).on("load error", function(){
            $("#progress-text").text(Math.round((hasLoadedCount++ + 1) / imgSrcArrLen * 100) + "%");
            if(index >= imgSrcArrLen-1){
                window.location.href = "./travel.html";
            }
        });
		imgObj.src = imgSrc;
	});
}
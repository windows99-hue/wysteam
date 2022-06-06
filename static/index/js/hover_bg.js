var iBase = {
	Id: function(name) {
		return document.getElementById(name);
	},
	//设置元素透明度,透明度值按IE规则计,即0~100 
	SetOpacity: function(ev, v) {
		ev.filters ? ev.style.filter = 'alpha(opacity=' + v + ')' : ev.style.opacity = v / 100;
	}
}

//淡入效果(含淡入到指定透明度) 
function fadeIn(elem, speed, opacity) {
	/* 
	 * 参数说明 
	 * elem==>需要淡入的元素 
	 * speed==>淡入速度,正整数(可选) 
	 * opacity==>淡入到指定的透明度,0~100(可选) 
	 */
	speedspeed = speed || 20;
	opacityopacity = opacity || 100;
	//显示元素,并将元素值为0透明度(不可见) 
	elem.style.display = 'block';
	iBase.SetOpacity(elem, 0);
	//初始化透明度变化值为0 
	var val = 0;
	//循环将透明值以5递增,即淡入效果 
	(function() {
		iBase.SetOpacity(elem, val);
		val += 5;
		if (val <= opacity) {
			setTimeout(arguments.callee, speed)
		}
	})();
}

//淡出效果(含淡出到指定透明度) 
function fadeOut(elem, speed, opacity) {
	/* 
	 * 参数说明 
	 * elem==>需要淡入的元素 
	 * speed==>淡入速度,正整数(可选) 
	 * opacity==>淡入到指定的透明度,0~100(可选) 
	 */
	speedspeed = speed || 20;
	opacityopacity = opacity || 0;
	//初始化透明度变化值为0 
	var val = 100;
	//循环将透明值以5递减,即淡出效果 
	(function() {
		iBase.SetOpacity(elem, val);
		val -= 5;
		if (val >= opacity) {
			setTimeout(arguments.callee, speed);
		} else if (val < 0) {
			//元素透明度为0后隐藏元素 
			elem.style.display = 'none';
		}
	})();
}

window.onload = function() {
	var main = document.getElementById("main");
	var wys_tools = document.getElementById("wys-tools");
	var soft_download = document.getElementById("soft-download");
	var vmos_zhuan = document.getElementById("vmos-zhuan");
	var about = document.getElementById("about");
	soft_download.onmouseover = function() {
		// 3.事件处理程序
		main.style.backgroundImage = "url(/static/index/img/01-.jpg)";
	}
	// 鼠标移开事件
	soft_download.onmouseout = function() {
		// 3.事件处理程序
		main.style.backgroundImage = "url(/static/index/img/bg.jpg)";
	}


	vmos_zhuan.onmouseover = function() {
		// 3.事件处理程序
		main.style.backgroundImage = "url(/static/index/img/02.jpg)";
	}
	// 鼠标移开事件
	vmos_zhuan.onmouseout = function() {
		// 3.事件处理程序
		main.style.backgroundImage = "url(/static/index/img/bg.jpg)";
	}


	about.onmouseover = function() {
		// 3.事件处理程序
		main.style.backgroundImage = "url(/static/index/img/about_bg.jpg)";
	}
	// 鼠标移开事件
	about.onmouseout = function() {
		// 3.事件处理程序
		main.style.backgroundImage = "url(/static/index/img/bg.jpg)";
	}
};

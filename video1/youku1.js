var VIP_CONFIG = {
	action: {
		get_member_info: '//vip.youku.com/ajax/member/get_member_info.jsonp', //获取用户基本信息
		vip_recomend: '//vip.youku.com/ajax/member/get_guess_likes.jsonp?callback=?', //为你推荐（猜你喜欢）
		hot_rank: '//vip.youku.com/svip/hot_broadcast_rank.jsonp?callback=?', //热播排行
		// 电影筛选
		movie_tag: '//vip.youku.com/ajax/filter/show_filter', //筛选标签
		movie_data: '//vip.youku.com/ajax/filter/filter_data', //电影电视剧等筛选结果
		trade_list: '//vip.youku.com/ajax/premium/get_my_trade_list.jsonp', //交易记录
		trade_detail: '//vip.youku.com/ajax/premium/trade_detail.jsonp?callback=?', //获取交易详情
		trade_cancel: '//vip.youku.com/ajax/premium/cancle_order.jsonp?callback=?', //取消订单
		trade_remind: '//vip.youku.com/ajax/premium/send_remind.jsonp?callback=?', //提醒发放权益
		speed_up: '//vip.youku.com/?c=ajax&a=ajax_do_speed_up', //宽带加速
		switch_service_url: '//vip.youku.com/?c=ajax&a=ajax_speedup_service_switch', //加速服务开关
		speed_status: '//vip.youku.com/ajax/speedup/get_status.jsonp?callback=?', //用户的宽带加速状态判断
		packageCheck: '//vip.youku.com/svip/get_xml.jsonp?cid=231977&callback=?', //会员套餐设置
		fls_welfare: '//vip.youku.com/ajax/welfare/get_welfare_list', //福利列表
		my_welfare: '//vip.youku.com/ajax/welfare/get_my_welfare_list', //我的福利列表
		get_welfare: '//vip.youku.com/ajax/welfare/send_welfare',
		//会员卡激活
		activeCard: '//vip.youku.com/ajax/premium/verify_card.jsonp?', //会员卡激活
		getVcode: '//vip.youku.com/ajax/message/send_sms.jsonp?', // 绑定手机号发送短信
		isHasPhone: '//vip.youku.com/ajax/member/get_user_info_by_ytid.jsonp?', //是否有手机号  
		bind_ticket: '//vip.youku.com/ajax/premium/bind_ticket.jsonp?callback=?', //添加观影券
		get_captcha: '//captcha.youku.com/captcha/get_captcha', //获取图片验证码
		get_my_ticket_list: '//vip.youku.com/ajax/premium/get_my_ticket_list.jsonp?callback=?', //获取观影券列表
		get_welfare_info: '//vip.youku.com/ajax/welfare/get_welfare_info.jsonp?', //获取福利详情
		index_notice: '//vip.youku.com/ajax/message/sys_notice', //会员公告
		movie_calender: '//vip.youku.com/ajax/calendar/get_list.jsonp?callback=?', //会员日历
		calender_subscribe: '//vip.youku.com/ajax/calendar/prev_user.jsonp?callback=?' //会员日历订阅

	},
	cms: {
		recomend_txt: '//vip.youku.com/vips/cms/212929.shtml', //续费推荐文本
		index_banner: '//vip.youku.com/vips/cms/217749.shtml', //首页轮播大图
		lastest_online: '//vip.youku.com/vips/cms/214466.shtml', //最新上线
		coming_movie: '//vip.youku.com/vips/cms/212927.shtml', //即将上线
		vip_club: '//vip.youku.com/vips/cms/212923.shtml', //会员俱乐部

		welfare: '//vip.youku.com/vips/cms/212925.shtml', //会员特惠与会员福利
		live: '//vip.youku.com/vips/cms/212926.shtml', //直播
		vip_theater: '//vip.youku.com/vips/cms/214851.shtml', //会员剧场
		original_movie: '//vip.youku.com/vips/cms/214168.shtml', //原创抢先看
		time_2017: '//vip.youku.com/vips/cms/251361.shtml', //时间的朋友2017
		knowledge_pay: '//vip.youku.com/vips/cms/253180.shtml', //新知付费
		knowledge_slider: '//vip.youku.com/vips/cms/253183.shtml', //新知轮播图
		knowledge_culture: '//vip.youku.com/vips/cms/253182.shtml', //新知人文国学
		knowledge_economic: '//vip.youku.com/vips/cms/253184.shtml', //新知经济财经
		knowledge_life: '//vip.youku.com/vips/cms/253188.shtml', //新知品质生活
		knowledge_career: '//vip.youku.com/vips/cms/253190.shtml', //新知职业发展
		knowledge_baby: '//vip.youku.com/vips/cms/253191.shtml', //新知亲子育儿
		micro_film: '//vip.youku.com/vips/cms/215353.shtml', //微电影
		deyunshe_mv: '//vip.youku.com/vips/cms/221282.shtml', //德云相声
		challenge_mv: '//vip.youku.com/vips/cms/245360.shtml', //我们的挑战会员版
		xinfan_mv: '//vip.youku.com/vips/cms/215354.shtml', //新番部屋
		documentary_mv: '//vip.youku.com/vips/cms/221075.shtml', //顶级记录
		//纪录片页面
		hotRankList: '//vip.youku.com/svip/list_show.jsonp?mg=13&o=4&pl=10&callback=?', //热播排行
		video_categories: '//vip.youku.com/vips/cms/234629.shtml', //视频分类
		awards_videos: '//vip.youku.com/vips/cms/234739.shtml', //获奖大片
		explore_discover: '//vip.youku.com/vips/cms/234742.shtml', //探索发现
		social_humanity: '//vip.youku.com/vips/cms/234743.shtml', //社会人文
		more_wonderful: '//vip.youku.com/vips/cms/234745.shtml', //更多精彩
		//我的会员  
		movie_ticket: '//vip.youku.com/ajax/filter/filter_data.jsonp?pt=2&tag=10005&pn=1&pl=6&callback=?', //观影券专享
		vip_welfare: '//vip.youku.com/index/welfare.jsonp?', //会员福利 Receive=1为当前可领，pn是条数
		life_privilege: '//vip.youku.com/ajax/welfare/get_privilege_life_list.jsonp?', //生活特权pszie 条数 pn 页数
		// movie_ticket: '//vip.youku.com/svip/list_show.jsonp?pt=2&callback=?', //观影券专享
		get_welfare_list: '//vip.youku.com/ajax/welfare/get_welfare_list.jsonp?', //福利列表 receive=1为当前可领，pszie是条数
		send_welfare: '//vip.youku.com/ajax/welfare/send_welfare.jsonp?', //福利领取
		//get_welfare_info: ' //vip.youku.com/ajax/welfare/get_welfare_info.jsonp?wid=60', //获取福利详情

		// 电影筛选页
		tv_banner: '//vip.youku.com/vips/cms/236465.shtml', //看剧banner
		animation_banner: '//vip.youku.com/vips/cms/236466.shtml', //动漫banner
		log_banner: '//vip.youku.com/vips/cms/236464.shtml', //纪录片banner
		movie_banner: '//vip.youku.com/vips/cms/236463.shtml', //电影banner
		//看电影页面
		movie_type: '//vip.youku.com/ajax/filter/show_filter?tag=10005', //电影类型列表
		hot_movie: '//vip.youku.com/vips/cms/235346.shtml', //热门电影
		week_swing: '//vip.youku.com/vips/cms/235364.shtml', //一周热播
		exclusive_plan: '//vip.youku.com/vips/cms/235365.shtml', //独家策划
		high_score: '//vip.youku.com/vips/cms/235366.shtml', //品，不可错过的高分佳作
		wave: '//vip.youku.com/vips/cms/235367.shtml', //浪，欲拒还迎蠢蠢欲动
		dazzle: '//vip.youku.com/vips/cms/235368.shtml', //炫，视觉离开地球表面
		burn: '//vip.youku.com/vips/cms/235369.shtml', //燃，拳拳到肉枪枪溅血
		crown: '//vip.youku.com/vips/cms/235370.shtml', //颠,醉痴疯傻乱世浮生
		coldOff: '//vip.youku.com/vips/cms/235371.shtml', //凉，午夜幽怨曲异度空间
		theBest: '//vip.youku.com/vips/cms/212927.shtml', //佳片有约
		// 德云社
		deyunshe: '//vip.youku.com/vips/cms/deyunshe.shtml',
		//会员直播
		vip_live: '//vip.youku.com/vips/cms/238019.shtml', //直播轮播图
		vip_livePast: '//vip.youku.com/vips/cms/212899.shtml', //直播列表
		silver_theater: '//vip.youku.com/vips/cms/214667.shtml', //优酷体验会员剧场

        //ezone
        ezone_slide: '//vip.youku.com/vips/cms/251608.shtml', //ezone轮播图
        ezone_show: '//vip.youku.com/vips/cms/251615.shtml', //劲爆真人秀
        ezone_hot: '//vip.youku.com/vips/cms/251613.shtml', //强档热播
        ezone_last_movie: '//vip.youku.com/vips/cms/251481.shtml' //Ezone6排图

	}
};
// 从土豆会员中心跳转到优酷，需要将优酷的头部一些模块隐藏
(function() {
	var domReady, addEvent, preventDefault, rerewriteHrefReg = /vip.youku.com\/vips/;
	// rerewriteHrefReg = /(static.youku.com)|(vip.youku.com\/vips)/;
	// 获取浏览器地址栏key value
	function getKeyVal(str) {
		// var str = location.search;
		if (str.indexOf('?') === -1) {
			return {};
		}
		str = str.slice(str.indexOf('?'));
		if (str.length === 1) {
			return {};
		} else {
			str = str.slice(1);
		}
		var keyValArr = str.split('&'),
			i, j, result = {},
			cache;
		if (!keyValArr.length) {
			return result;
		}
		for (i = 0, j = keyValArr.length; i < j; i++) {
			cache = keyValArr[i].split('=');
			result[cache[0]] = cache[1];
		}
		return result;
	}
	// domready
	domReady = function() {
		var readyReg = /complete|loaded|interactive/; //interactive 
		var ready = function(callback) {
			// for ie
			if (readyReg.test(document.readyState) && document.body) {
				callback();
			} else {
				document.addEventListener('DOMContentLoaded', function() {
					callback();
				}, false);
			}
		};
		return ready;
	}();

	addEvent = function() {
		if (document.addEventListener) {
			return function(ele, eType, callback) {
				ele.addEventListener(eType, callback, false);
			};
		} else if (document.attachEvent) {
			return function(ele, eType, callback) {
				ele.attachEvent('on' + eType, function() {
					callback.call(ele, window.event);
				});
			};
		} else {
			ele['on' + eType] = callback;
		}
	}();
	preventDefault = function(event) {
		if (event.preventDefault) {
			return event.preventDefault();
		}
		if (window.event.returnValue) {
			return window.event.returnValue = false;
		}
	};
	domReady(function() {
		var $body = document.body,
			referrer = location.href;
		if (getKeyVal(referrer).from === 'tudou') {
			var bodyClass = $body.getAttribute('class');
			if (!bodyClass) {
				$body.setAttribute('class', 'tudou');
			} else {
				$body.setAttribute('class', bodyClass + ' tudou');
			}
			addEvent(document.body, 'click', function(e) {
				var target = e.srcElement || e.target,
					href, pre = '';

				if (target.tagName.toLowerCase() === 'a') {
					href = target.getAttribute('href');
					if (rerewriteHrefReg.test(href)) {
						preventDefault(e);
						if (href.indexOf('?') !== -1 && href.lastIndexOf('?') !== (href.length - 1)) {
							pre = '&';
						} else if (href.indexOf('?') === -1) {
							pre = '?';
						}
						location.href = href + pre + 'from=tudou';
					}
				}
			});
		}
	});
})();

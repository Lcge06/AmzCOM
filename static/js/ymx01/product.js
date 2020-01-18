/*
LCG 20191213
 */

function ResetStyle() {
    $('#ProductPicList div a').removeClass('current');
}
//鼠标移动到小图上显示大图
$(function () {
    $('#ProductPicList div a').bind('mouseover',function () {
        ResetStyle();
        $(this).addClass('current');
        $('#MainImg img').attr('src',$(this).find('img').attr('src'));
    })
})
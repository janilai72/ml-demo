#coding=utf8
##{B（词开头），M（词中），E（词尾），S（独字词）} {0,1,2,3}
data=[{
 u"我要吃饭":"SSBE"},
{
u"天气不错" : "BEBE"},
{
u"谢天谢地" : "BMME"}]
#O： 观察对象的集合， 这里是字的集合，{我要吃饭天气不错谢天地}
#S: 隐藏状态集合，这里是{BMES}
SortDoubanSearchResult
======================
#中文说明
想找本评价很高的python书来看，在豆瓣上一搜，结果完全是无序的（对我来说，对服务端来说肯定是有顺序的），
我需要按评分来排序搜索结果，可惜豆瓣页面上没找到类似的功能，于是自己写了个脚本，自动抓取搜索结果，
然后根据评分由高到低排序，并生成一个本地html文件。

#使用说明
使用时要把douban.py里sort_search_result('毛姆')的参数改为需要搜索的书籍名称

#example
    <table>
		<tr>
			<td>#</td>
			<td>评分</td>
			<td>书名</td>
		</tr>
		<tr><td>1</td><td>9.2</td><td><a href="http://book.douban.com/subject/4123116/">月亮和六便士</a> <span style="font-size:10pt">
        
  
  [英] 毛姆 / 傅惟慈 / 上海译文出版社 / 2009-10 / 32.00元

      </span></td></tr>
<tr><td>2</td><td>9.2</td><td><a href="http://book.douban.com/subject/1025917/">刀锋</a> <span style="font-size:10pt">
        
  
  （英）毛姆 / 戴珩 / 少年儿童出版社 / 2001-8 / 9.00

      </span></td></tr>
<tr><td>3</td><td>9.1</td><td><a href="http://book.douban.com/subject/10774752/">毛姆短篇小说精选集</a> <span style="font-size:10pt">
        
  
  (英)威廉·萨默塞特·毛姆 / 冯亦代、傅惟慈、陆谷孙 / 译林出版社 / 2012-11 / 36.00元

      </span></td></tr>
<tr><td>4</td><td>9.1</td><td><a href="http://book.douban.com/subject/3540588/">月亮与六便士: 毛姆文集</a> <span style="font-size:10pt">
        
  
  [英]毛姆 / 傅惟慈 / 上海译文出版社 / 1995-12 / 15.80元

      </span></td></tr>
      </table>

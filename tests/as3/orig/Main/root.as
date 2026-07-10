
//3i flash.Lib

/*3

i flash.display.BitmapData
m ../a.png MyBitmapData

a Main
	f s
		g stage
*/
		var texture=flash.display.BitmapData.loadBitmap('MyBitmapData');//3 m

		attachMovie('MyClip','shape',getNextHighestDepth());
		shape._x = (Stage.width - 100) / 2;
		shape._y = (Stage.height - 100) / 2;
		/*3d shape stage

c		var img = new Bitmap( new MyBitmapData(0, 0) );
c		Lib.current.addChild(img);
	}
}
*/
/*more tests
function ()()//3 e+e
begin(a);_x//3 l q+s
var texture=flash.display.BitmapData._loadBitmap('MyBitmapData');//3 s+m
useHandCursor=_x;//3
useHandCursor=_x;//3 b+s
onEnterFrame=_fune;//3 o+s
_alpha=_x;//3 p+s
line(_width,_y);line(_width,_height);line(_x,_height);//3 r q+s
_x()//3 s+e
_y()//3 s _+e
create('q',n,_x,_y,_width,_height);//3 t+s
attach('q','_p',d);//3 v+s
_leftPart='type';//3 x+s
*/

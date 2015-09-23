<?php
$im = imagecreatefromjpeg("image.jpeg");
$red = 0;
$blue = 0;
$green = 0;
$size = getimagesize("image.jpeg");
for($i=0;$i<$size[0];$i++)
{
	for($j=0;$j<$size[1];$j++)
	{
		$rgb = imagecolorat($im, $i, $j);
		$colors = imagecolorsforindex($im, $rgb);
		$red = $red + $colors["red"];
		$blue = $blue + $colors["blue"];
		$green = $green + $colors["green"];
	}
}
if(isset($_GET["red"]))
	echo intval(($red/($size[0]*$size[1])));
if(isset($_GET["green"]))
	echo intval(($green/($size[0]*$size[1])));
if(isset($_GET["blue"]))
	echo intval(($blue/($size[0]*$size[1])));
?>
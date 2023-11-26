import scala.io.Source

case class Track(title: String, length: String, rating: Int, features: List[String], writers: List[String])
case class Album(title: String, date: String, artist: String, tracks: List[Track])

val home = System.getProperty("user.home")
val albums = Source.fromFile(s"$home/IdeaProjects/untitled/alben.xml").toList

//Praktikum2
def parseTrack(source: List[String], TrackList: List[Track], myTrack: Track): List[Track] = source match {
  case "feature"::x::xs => parseTrack(xs, TrackList, myTrack.copy(features = myTrack.features :+ x))
  case "writing"::x::xs => parseTrack(xs, TrackList, myTrack.copy(writers =  myTrack.writers :+ x))
  case "title"::x::xs => parseTrack(xs, TrackList, myTrack.copy(title = x))
  case "length"::x::xs => parseTrack(xs, TrackList, myTrack.copy(length = x))
  case "rating"::x::xs => parseTrack(xs, TrackList, myTrack.copy(rating = x.toInt))
  case "/track"::xs => TrackList :+ myTrack
  case _::xs => parseTrack(xs, TrackList, myTrack)
  case Nil => Nil
}

def parseAlbum(source: List[String], myAlbum: Album):Album = source match {
  case "track"::xs => parseAlbum(xs, myAlbum.copy(tracks=parseTrack(xs, myAlbum.tracks, Track("","",0,Nil,Nil))))
  case "title"::x::xs => parseAlbum(xs, myAlbum.copy(title=x))
  case "artist"::x::xs => parseAlbum(xs, myAlbum.copy(artist=x))
  case "date"::x::xs => parseAlbum(xs, myAlbum.copy(date=x))
  case "/album"::xs => myAlbum
  case _::xs => parseAlbum(xs, myAlbum)
  case Nil => myAlbum
}

def parseFile(source:List[String]): List[Album] = source match {
  case "album"::xs => parseAlbum(xs, Album("","","",Nil))::parseFile(xs)
  case _::xs => parseFile(xs)
  case Nil => Nil
}

def createTokenListInsideBracket(album: List[Char], myString: String): String = album match {
  case Nil => ""
  case '>'::xs => myString
  case x::xs => createTokenListInsideBracket(xs, myString+x)
}


def createTokenListOutsideBracket(album: List[Char], myString: String):String = album match {
  case Nil => ""
  case '<'::xs => myString
  case x::xs => createTokenListOutsideBracket(xs, myString+x)
}

def createTokenList(album: List[Char]): List[String] = album match {
  case Nil => Nil
  case '<'::xs => createTokenListInsideBracket(xs, "") :: createTokenList(xs)
  case '>'::xs => createTokenListOutsideBracket(xs, "") :: createTokenList(xs)
  case _::xs => createTokenList(xs)
}

val Zwischen = createTokenList(albums)
val Endergebnis = parseFile(Zwischen)
println(Endergebnis)

//Praktikum 3
//1.a)
def map[A](func: A=>A, input_list:List[A]):List[A] = input_list match {
  case Nil => Nil
  case y::ys => func(y)::map(func,ys)
}

//1.b)
val Ergebnis1b = map[Album](x => x.copy(title = x.title.toUpperCase), Endergebnis)

//1.c)
val Ergebnis1c = map[Album](x => {val aktuellesAlbum = x.copy(title = x.title.toUpperCase); aktuellesAlbum.copy(tracks = map[Track](x => x.copy(title = x.title.toUpperCase), x.tracks))}, Endergebnis)

//1.d)
def poly_map[A,B](func: A=>B, input_list:List[A]):List[B] = input_list match {
  case Nil => Nil
  case y::ys => func(y)::poly_map(func,ys)
}

//1.e)
val Ergebnis1e = poly_map[Album, List[String]](x => poly_map[Track, String](x => x.length, x.tracks), Endergebnis)

//2.a)
val MichaelJackson = Endergebnis(1)

def filter [A](condition: A=>Boolean, input_list: List[A]):List[A] = input_list match{
  case Nil => Nil
  case y::ys => if(condition(y))  y::filter(condition,ys)  else  filter(condition,ys)
}

//2.b)
val Ergebnis2b = filter[Track](x => x.rating >= 4, MichaelJackson.tracks)

//2.c)
val Ergebnis2c = poly_map[Track, String](x => x.title, filter[Track](x => x.writers.contains("Rod Temperton"), MichaelJackson.tracks ))

//3.a)
def partition[A](condition: A => Boolean, input_list: List[A]): List[List[A]] =  input_list match {
  case Nil => List(List())
  case x::xs => condition(x) match {
    case true => List()::partition(condition, xs)
    case false =>  val y = partition(condition, xs); (x::y.head)::y.tail
  }
}

//3.b)
val Ergebnis3b = partition[String](x => x == "Thriller", poly_map[Track, String](x => x.title, MichaelJackson.tracks))

//3.c)
def isBlank(s:String):Boolean = s.trim.isEmpty
val Partition3c1 = partition[Char](x =>  (x == '<') || (x == '>') , albums)
val Poly_Map3c2 = poly_map[List[Char],String](x => x.mkString, Partition3c1 )
val Filter3c3 = filter[String](x => !(x.isBlank), Poly_Map3c2)

//4.a)
def calculate(f: Int => Int, concat:(Int, Int)=>Int, start: Int, a:Int, b:Int):Int =
  if (a>b) start else concat(f(a), calculate(f, concat, start, a+1, b))

/*
//4.b) plus(a, plus(a2, plus(a3, plus(a4, plus(b, n)))))
Q1: Welches Folding wird verwendet?
A1: right-folding -> bsp: 1 + (2 + (3 + (4 + 5))) statt left-folding -> bsp: (((1 + 2) + 3) + 4) + 5

Q2: Unter welchen Umständen würde left-folding die Funktionalität des Programms ändern?
A2: Die Funktionalität wäre die gleiche nur die Reihenfolge der Funktionsaufrufe bzw.
          der Klammerung ist unterschiedlich.
*/

/*
//4.c)
Q1: Wie verhält sich die Implementierung aus Aufgabe 4.a) für einen leeren Wertebereich?
A1: Bei einem Wertebereich von "null" gibt es eine Fehlermeldung. Bei einem Wertebereich
von bsp. 2 bis 2 wird mit der Zahl zwei gerechnet.

Q2: Welches Verhalten wäre bei einem leeren Wertebereich sinnvoll?
A2: Eine Fehlermeldung wäre sinnvoll, die aussagt, dass der Wertebereich leer ist.
*/

//4.d)
def foldr(f:(Int,Int) => Int, start: Int, xs: List[Int]) : Int =
xs match {
  case Nil => start
  case y::ys => f(foldr(f,start,ys),y)
}
def range(a:Int,b:Int) : List[Int] = if (a>b) Nil else a::range(a+1,b)

val Ergebnis4a = calculate(x=>x, (a,b)=>a*b,1, 1, 5)
val Ergebnis4d = foldr((x,y)=>x*y,1,map[Int](x=>x, range(1,5)))

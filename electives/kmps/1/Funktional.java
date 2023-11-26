import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;


public class Funktional {
	
	public static ArrayList<String> createTokenList(byte[] file_contents, ArrayList<String> token_list, int current_character){
		if(current_character < file_contents.length){
			if (file_contents[current_character] == '\n' || file_contents[current_character] == '\r' || file_contents[current_character] == '\t') {
				return createTokenList(file_contents, token_list, current_character+1);
			}	
			else if (file_contents[current_character] == '<'){ 
				return createTokenHelper(file_contents, token_list,  current_character+1, "");
			}
			else {
				return createTokenHelper(file_contents, token_list, current_character, "");
			}
		}
			return token_list;	
	}

	public static ArrayList<String>createTokenHelper(byte[] file_contents, ArrayList<String> token_list, int current_character, String token){
		if(current_character < file_contents.length){
			if(file_contents[current_character] == '<' || file_contents[current_character] == '>') {
				token_list.add(token);
				return createTokenList(file_contents, token_list, current_character+1);
			}else {
				token = token+(char)file_contents[current_character];
				return createTokenHelper(file_contents, token_list, current_character+1, token);
			}
		}
		return createTokenList(file_contents, token_list, current_character+1); 
	}
	
	public static ArrayList<Album> parseFile(ArrayList<String> album_tokenliste, ArrayList<Album> albums, boolean is_in_album, boolean is_in_track, int current_album, int current_track, int counter){
		if(counter < album_tokenliste.size())
		{
			
			if(album_tokenliste.get(counter).equals("album")) {
				
				albums.add(new Album());
				
				return parseFile(album_tokenliste, albums, true, is_in_track, albums.size()-1, current_track, counter+1); 
			}
			
			else if(album_tokenliste.get(counter).equals("/album")){
				return parseFile(album_tokenliste, albums, false, is_in_track, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("title")){
				if(is_in_track) {
					albums.get(current_album).tracks.get(current_track).title = album_tokenliste.get(counter+1); 
				}
				
				else if(is_in_album) {
					albums.get(current_album).title = album_tokenliste.get(counter+1); 
				}
				
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("artist")){
				albums.get(current_album).artist = album_tokenliste.get(counter+1);
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("rating")){
				albums.get(current_album).tracks.get(current_track).rating = Integer.parseInt(album_tokenliste.get(counter+1));
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("track")){
				albums.get(current_album).tracks.add(new Track());
				return parseFile(album_tokenliste, albums, is_in_album, true, current_album, albums.get(current_album).tracks.size()-1, counter+1); 
			}
			
			else if(album_tokenliste.get(counter).equals("/track")) {
				return parseFile(album_tokenliste, albums, is_in_album, false, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("feature")) {
				albums.get(current_album).tracks.get(current_track).features.add(album_tokenliste.get(counter+1));
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("length")) {
				albums.get(current_album).tracks.get(current_track).length = album_tokenliste.get(counter+1);
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("writing")) {
				albums.get(current_album).tracks.get(current_track).writers.add(album_tokenliste.get(counter+1));
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
			
			else if(album_tokenliste.get(counter).equals("date")) {
				albums.get(current_album).date = album_tokenliste.get(counter+1);
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
			
			else {
				return parseFile(album_tokenliste, albums, is_in_album, is_in_track, current_album, current_track, counter+1);
			}
		}
		return albums;
	}
	
	public static void main(String[] args) throws IOException {
		
		ArrayList<Album> albums = new ArrayList<Album>();
		ArrayList<String> album_tokenliste = new ArrayList<String>();
		byte[] file_contents = Files.readAllBytes(Paths.get("alben.xml"));
		
		album_tokenliste = createTokenList(file_contents, album_tokenliste, 0);
		albums = parseFile(album_tokenliste, albums, false, false, 0, 0, 0);
		
		
		for(int i = 0; i < albums.size(); i++){
			System.out.println(albums.get(i));
		}
	}
}
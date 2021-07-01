"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._all_vids = VideoLibrary.get_all_videos() 
        self._all_vids.sort()
        self._vid_ids = []
        self._vid_list = []
        for vid in self._all_vids:
            self._vid_ids.append(vid.video_id)
        self._playing = False
        self._current = None
        self._pause = False
        
    
    def number_of_videos(self):
        num_videos = len(self._all_vids())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
        print("Here's a list of all available videos:\n")
        for vid in self._all_vids:
            print(f"{vid.title} (", f"{vid.video_id}) [", f"{vid.tags}]\n")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        if video_id not in self._vid_ids:
            print("Cannot play video: Video does not exist")
        else:
            self._playing = True
            self._current = self._video_library.get_video(video_id)
            play_title = self._current.title
            print("Playing video: ", f"{play_title}")

    def stop_video(self):
        """Stops the current video."""
        if self._playing == False:
            print("Cannot stop video: No video is currently playing")
        else:
            self._playing = False
            play_title = self._current.title
            print("Stopping video: ", f"{play_title}")
            self._current = None
            

    def play_random_video(self):
        """Plays a random video from the video library."""
        """
        self._all_vids 
        delete from list
        
        play and stop video
        """
                

    def pause_video(self):
        """Pauses the current video."""
        
        
        '''
        check if theres video playing
        if loop
        self._pause = True
        '''


    def continue_video(self):
        """Resumes playing the current video."""
        '''
        self._pause = False
        '''

    def show_playing(self):
        """Displays video currently playing."""

        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

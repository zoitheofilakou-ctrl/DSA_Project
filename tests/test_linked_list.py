from data_structures.linked_list import LinkedList

def test_add_three_songs():
    playlist = LinkedList()
    playlist.add("Imagine")
    playlist.add("Black Sabbath")
    playlist.add("Hotel California")

    # Check the first node
    assert playlist.head.data == "Imagine"
    # Check the second node
    assert playlist.head.next.data == "Black Sabbath"
    # Check the third node
    assert playlist.head.next.next.data == "Hotel California"
    # The last node should point to None
    assert playlist.head.next.next.next is None


def test_remove_first_song():
    playlist = LinkedList()
    playlist.add("Imagine")
    playlist.add("Black Sabbath")
    playlist.add("Hotel California")

    playlist.remove_first()
    # After removal, the first node should now be "Black Sabbath"
    assert playlist.head.data == "Black Sabbath"
    assert playlist.head.next.data == "Hotel California"


def test_remove_first_from_empty_list():
    playlist = LinkedList()
    # Removing from an empty list should not raise an error
    playlist.remove_first()
    assert playlist.head is None


def test_add_after_removal():
    playlist = LinkedList()
    playlist.add("Imagine")
    playlist.remove_first()
    playlist.add("Let it be")

    # After removal and adding a new song,
    # the list only contain "Let it be"
    assert playlist.head.data == "Let it be"
    assert playlist.head.next is None

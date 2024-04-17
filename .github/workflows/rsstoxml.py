import feedparser
import sys

# Function to fetch and update RSS feed
def update_xml_feed(rss_url, output_file):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)
    
    # Write the feed content to the XML file
    with open(output_file, 'w') as xml_file:
        xml_file.write(str(feed))

# Main function
if __name__ == "__main__":
    # Check if command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <rss_url> <output_file>")
        sys.exit(1)
    
    rss_url = sys.argv[1]
    output_file = sys.argv[2]
    
    # Update XML feed
    update_xml_feed(rss_url, output_file)

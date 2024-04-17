import feedparser

# Function to fetch and update RSS feed
def update_xml_feed(rss_url, output_file):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)
    
    # Write the feed content to the XML file
    with open(output_file, 'w') as xml_file:
        xml_file.write(str(feed))

# Main function
if __name__ == "__main__":
    rss_url = "https://www.zuiderzeeland.nl/rss/content-list?type%5B%5D=page&type%5B%5D=vacancy&tags%5B%5D=932&sort_by=changed&sort_order=DESC"
    output_file = "vacature_zzl.xml"
    
    # Update XML feed
    update_xml_feed(rss_url, output_file)

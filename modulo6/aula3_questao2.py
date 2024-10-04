URLs = ['www.facebook.com', 'www.twitter.com','www.microsoft.com','www.apple.com','www.netflix.com','www.amazon.com','www.spotify.com','www.linkedin.com','www.pinterest.com','www.twitch.com']

fatiamento = [dominio[4:-4] for dominio in URLs]

print(f'Nome das URLs: {fatiamento}')
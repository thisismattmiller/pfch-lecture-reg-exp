import re

text = "William Wegman, Cotto, 1970. Gelatin silver print 1971, 7 7/8 × 7 3/4 in. (20 × 19.7 cm). Whitney Museum of American Art, New York; purchase with funds from the Mrs. Percy Uris Purchase Fund and the Photography Committee  92.14\n© William Wegman"

pattern = re.compile('[0-9]{4}')

results = pattern.findall(text)

print(results)
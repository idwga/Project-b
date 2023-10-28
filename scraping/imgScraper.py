from bs4 import *
import requests
import os
class run:
	print("")
ia = open("data/display/imgScrTit")
print(ia.read())

def folder_create(images,name):

	folder_name = 'downloads'

	download_images(images,name,folder_name)


def download_images(images,name,folder_name):

	count = 0

	print(f"Total {len(images)} Image Found!")

	if len(images) != 0:
		for i, image in enumerate(images):
			try:
				image_link = image["data-srcset"]
				
			except:
				try:
					image_link = image["data-src"]
				except:
					try:
						image_link = image["data-fallback-src"]
					except:
						try:
							image_link = image["src"]

						except:
							pass


			try:
				r = requests.get(image_link).content
				try:

					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					with open(f"{folder_name}/{name}{i+1}", "wb+") as f:
						f.write(r)

					count += 1
			except:
				pass


		if count == len(images):
			print("All Images Downloaded!")
		else:
			print(f"Total {count} Images Downloaded Out of {len(images)}")

def main(url,name):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	images = soup.findAll('img')
	folder_create(images,name)

a=0
while a==0:
	print("[a]Scrape images		[q]Quit")
	inp = input(":")
	if(inp=="a"):
		url = input("Enter URL: ")
		name = input("Enter image name: ")
		main(url,name)
		ea = open("data/display/imgScrOut")
		print(ea.read())
	if(inp=="q"):
		a+=1
	print("\n")
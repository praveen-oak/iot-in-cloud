import s3_operations
import rekognition

def main():
	bucket_name = "stockimages"
	# s3_operations.create_bucket(bucket_name)
        # s3_operations.upload_file("/Users/praveenoak/Downloads/cycling.jpg", bucket_name, "cycling")

        rekognition.recognise_image(bucket_name, "cycling")

if __name__== "__main__":
	main()

import os
import boto3

# fetch credentials from env variables
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

# setup a AWS S3 client/resource
s3 = boto3.resource(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# # point the resource at the existing bucket
# # bucket = s3.Bucket("anyoneai-ay22-01")
# bucket = s3.Bucket("anyoneai-datasets")  # anyoneai-datasets/SKU-110K/SKU110K_fixed


# # print all object names found in the bucket
# for file in bucket.objects.all():
#     if "SKU-110K" in file:
#         print(file)

# # download the training dataset
# with open('training_image_set.tgz', 'wb') as data:
#     bucket.download_fileobj('training-datasets/car_ims.tgz', data)
# # download the dataset labels
# with open('car_dataset_labels.csv', 'wb') as data:
#     bucket.download_fileobj('training-datasets/car_dataset_labels.csv', data)


from pathlib import Path

# s3 = boto3.resource("s3")

bucket = s3.Bucket("bucket")

key = "anyoneai-datasets/SKU-110K/SKU110K_fixed/"
objs = list(bucket.objects.filter(Prefix=key))

for obj in objs:
    # print(obj.key)

    # remove the file name from the object key
    obj_path = os.path.dirname(obj.key)

    # create nested directory structure
    Path(obj_path).mkdir(parents=True, exist_ok=True)

    # save file with full path locally
    # bucket.download_file(obj.key, obj.key)
    print(obj.key)

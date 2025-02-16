#!/bin/bash

SERVER="http://192.168.2.5:5000"
TEST_FOLDER="myfolder"
TEST_FILE="largefile.pdf"
TEST_TEXT="notes.txt"
TEST_IMAGE="photo.jpg"

echo "Checking API Endpoints on $SERVER..."
echo "======================================"

# 1. Check File Listing
echo "Checking /files..."
curl -s -X GET "$SERVER/files" | jq . || echo "ERROR: /files failed"

# 2. Check File Upload (largefile.pdf)
echo "Uploading $TEST_FILE..."
curl -s -X POST -F "file=@$TEST_FILE" "$SERVER/upload" | jq . || echo "ERROR: Upload failed"

# 3. Check File Download
echo "Downloading $TEST_FILE..."
curl -s -o /dev/null -w "%{http_code}\n" "$SERVER/download/$TEST_FILE" || echo "ERROR: Download failed"

# 4. Check File Deletion
echo "Deleting $TEST_FILE..."
curl -s -X DELETE "$SERVER/delete/$TEST_FILE" | jq . || echo "ERROR: Delete failed"

# 5. Check File Renaming
echo "Renaming $TEST_TEXT to new_notes.txt..."
curl -s -X PUT "$SERVER/rename?old_name=$TEST_TEXT&new_name=new_notes.txt" | jq . || echo "ERROR: Rename failed"

# 6. Check Search Function
echo "Searching for 'notes'..."
curl -s -X GET "$SERVER/search?query=notes" | jq . || echo "ERROR: Search failed"

# 7. Check Folder Creation
echo "Creating folder $TEST_FOLDER..."
curl -s -X POST "$SERVER/mkdir?name=$TEST_FOLDER" | jq . || echo "ERROR: Folder creation failed"

# 8. Check Folder Deletion
echo "Deleting folder $TEST_FOLDER..."
curl -s -X DELETE "$SERVER/rmdir?name=$TEST_FOLDER" | jq . || echo "ERROR: Folder deletion failed"

# 7. Check Folder Creation
echo "Creating folder $TEST_FOLDER..."
curl -s -X POST "$SERVER/mkdir?name=$TEST_FOLDER" | jq . || echo "ERROR: Folder creation failed"

# 9. Check File Preview (Image)
echo "Previewing $TEST_IMAGE..."
curl -s -o /dev/null -w "%{http_code}\n" "$SERVER/preview/$TEST_IMAGE" || echo "ERROR: Image preview failed"

# 10. Check Moving a File
echo "Moving new_notes.txt to $TEST_FOLDER..."
curl -s -X POST "$SERVER/move?file=new_notes.txt&to=$TEST_FOLDER" | jq . || echo "ERROR: Move failed"

# 11. Check API Statistics
echo "Checking API Stats..."
curl -s -X GET "$SERVER/stats" | jq . || echo "ERROR: Stats failed"

# 12. Check ZIP Folder Download
echo "Downloading folder $TEST_FOLDER as ZIP..."
curl -s -o /dev/null -w "%{http_code}\n" "$SERVER/zip?folder=$TEST_FOLDER" || echo "ERROR: ZIP download failed"

echo "All checks completed!"


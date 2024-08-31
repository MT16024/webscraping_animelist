# webscraping_animelist
Dự án này là một công cụ thu thập dữ liệu anime từ web, được xây dựng bằng Python sử dụng các thư viện như BeautifulSoup và Requests. Công cụ này trích xuất và tổng hợp dữ liệu từ nhiều trang web anime, tạo ra một cơ sở dữ liệu anime toàn diện và cập nhật, phục vụ cho phân tích, sưu tầm, hoặc gợi ý anime.

# Kết quả minh hoạ
<img width="701" alt="minhhoa" src="https://github.com/user-attachments/assets/9e0056a7-633d-43c2-99cf-6bff3abbbab2">


# Tính năng
* Trích xuất dữ liệu Anime: Thu thập các thông tin như tên anime, thể loại, đánh giá, tóm tắt nội dung, số tập, và ngày phát hành.
* Hỗ trợ nhiều trang web: Tương thích với nhiều trang web anime phổ biến, đảm bảo cơ sở dữ liệu đa dạng và phong phú.
* Tùy chỉnh thu thập dữ liệu: Cho phép người dùng chỉ định loại dữ liệu cần thu thập và từ trang web nào.
* Lưu trữ dữ liệu: Lưu trữ dữ liệu đã trích xuất vào các định dạng có cấu trúc như CSV hoặc JSON để dễ dàng truy cập và phân tích thêm.
* Xử lý lỗi: Áp dụng các cơ chế xử lý lỗi mạnh mẽ để quản lý các vấn đề như trang web không hoạt động, thay đổi cấu trúc trang web, và lỗi kết nối.

# Cài đặt
Để sử dụng công cụ này, bạn cần cài đặt Python trên máy tính của mình. Clone repository và cài đặt các thư viện cần thiết:

```ruby
bash
Copy code
git clone https://github.com/tennguoidung/webscraping_animelist.git
cd webscraping_animelist
pip install -r requirements.txt
```

LƯU Ý: File requirements.txt bao gồm các thư viện sau:
* beautifulsoup4 (còn gọi là bs4): Được sử dụng để phân tích và xử lý cú pháp HTML.
* requests: Dùng để gửi các yêu cầu HTTP đến các trang web.
* openpyxl: Hỗ trợ làm việc với file Excel (.xlsx), giúp lưu trữ dữ liệu dưới định dạng bảng tính Excel.

# Sử dụng
Chạy script với các tùy chọn mong muốn:

```ruby
bash
Copy code
python main.py --site="trang_web_anime" --output="anime_list.csv"
Các tùy chọn:
```

* site: Chỉ định trang web để thu thập dữ liệu.
* output: Định nghĩa tên và định dạng file đầu ra (CSV hoặc JSON).

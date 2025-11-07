# automatidata-tlc-project
Phân tích dữ liệu chuyên sâu (EDA) trên tập dữ liệu TLC của New York City nhằm xác định các yếu tố then chốt ảnh hưởng đến giá cước taxi, chuẩn bị nền tảng cho việc xây dựng ứng dụng ước tính giá cước

# Phân Tích Dữ Liệu và Khám Phá: Ước Tính Giá Cước Taxi NYC (Automatidata - TLC)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Project Status](https://img.shields.io/badge/Status-Course%202%20Complete-green.svg)]()

> **Tóm tắt ngắn:** Phân tích dữ liệu chuyên sâu (EDA) trên tập dữ liệu TLC của New York City nhằm xác định các yếu tố then chốt ảnh hưởng đến giá cước taxi, chuẩn bị nền tảng cho việc xây dựng ứng dụng ước tính giá cước.

## Bối Cảnh và Mục Tiêu Dự Án

### Bối Cảnh (Scenario)
Dự án này được thực hiện cho **Ủy ban Taxi và Limousine Thành phố New York (TLC)** theo đề xuất của công ty tư vấn dữ liệu **Automatidata**. Mục tiêu cuối cùng là phát triển một ứng dụng cho phép hành khách TLC **ước tính giá cước taxi trước chuyến đi**.

### Mục Tiêu Giai Đoạn (Course 2 Tasks)
Mục tiêu của giai đoạn này là xây dựng nền tảng phân tích vững chắc, bao gồm:
* Tải, làm sạch, và chuẩn bị tập dữ liệu TLC NYC.
* Sử dụng **Python** và **các hàm tùy chỉnh** để tổ chức dữ liệu hiệu quả.
* Thực hiện **Phân tích Dữ liệu Khám phá (EDA)** ban đầu để xác định các biến có ảnh hưởng lớn đến giá cước (`fare_amount`).
* Tạo **Tóm tắt Điều hành (Executive Summary)** cho nhóm Automatidata.

## Bộ Dữ Liệu và Các Biến Chính

## Bộ Dữ Liệu (Dataset)

### Nguồn Dữ Liệu
* **Nguồn:** Dữ liệu lịch sử chuyến đi của TLC New York City (được cung cấp cho mục đích học thuật/giả lập).
* **Kích thước:** Tập dữ liệu chứa **22,699 dòng** (mỗi dòng là một chuyến đi) và **18 cột**.

### Cấu Trúc Dữ Liệu (Column Descriptions)

| Tên Cột | Mô Tả |
| :--- | :--- |
| **ID** | Mã số định danh chuyến đi. |
| **VendorID** | Mã nhà cung cấp TPEP (1= Creative Mobile Technologies, 2= VeriFone Inc.). |
| **tpep_pickup_datetime** | Ngày và giờ đồng hồ được bật (bắt đầu chuyến đi). |
| **tpep_dropoff_datetime** | Ngày và giờ đồng hồ được tắt (kết thúc chuyến đi). |
| **Passenger_count** | Số lượng hành khách trong xe (giá trị do tài xế nhập). |
| **Trip_distance** | Khoảng cách chuyến đi đã đi (theo dặm/miles). |
| **PULocationID** | Mã Khu vực Taxi TLC (TLC Taxi Zone) nơi chuyến đi bắt đầu. |
| **DOLocationID** | Mã Khu vực Taxi TLC nơi chuyến đi kết thúc. |
| **RateCodeID** | Mã cước phí cuối cùng (1=Standard, 2=JFK, 3=Newark, v.v.). |
| **Store_and_fwd_flag** | Cờ báo hiệu chuyến đi được lưu tạm thời trên xe trước khi gửi đi (Y/N). |
| **Payment_type** | Hình thức thanh toán (1=Credit card, 2=Cash, 3=No charge, v.v.). |
| **Fare_amount** | **Tiền cước phí tính theo thời gian và khoảng cách** (biến mục tiêu chính). |
| **Extra** | Phụ phí linh tinh (bao gồm phụ phí giờ cao điểm $0.50 và $1.00). |
| **MTA_tax** | Thuế MTA $0.50 (tự động kích hoạt). |
| **Improvement_surcharge** | Phụ phí cải tiến $0.30 (tính khi bật đồng hồ). |
| **Tip_amount** | Tiền boa (chỉ tự động điền cho thẻ tín dụng, **không bao gồm tiền boa tiền mặt**). |
| **Tolls_amount** | Tổng số tiền cầu đường. |
| **Total_amount** | Tổng số tiền hành khách phải trả (không bao gồm tiền boa tiền mặt). |

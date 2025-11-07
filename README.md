# automatidata-tlc-project
Phân tích dữ liệu chuyên sâu (EDA) trên tập dữ liệu TLC của New York City nhằm xác định các yếu tố then chốt ảnh hưởng đến giá cước taxi, chuẩn bị nền tảng cho việc xây dựng ứng dụng ước tính giá cước

# Phân Tích Dữ Liệu và Khám Phá: Ước Tính Giá Cước Taxi NYC (Automatidata - TLC)

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Project Status](https://img.shields.io/badge/Status-Completed-green.svg)]()

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

## Bộ Dữ Liệu (Dataset) và Nguồn Gốc Dự Án

### Nguồn Gốc Dự Án
Dự án này là một phần của chuỗi nhiệm vụ học tập, được lấy cảm hứng từ khóa học:
* **Khóa học:** [Get Started with Python for Data Science](https://www.coursera.org/learn/get-started-with-python) trên nền tảng Coursera.
### Lưu Ý Quan Trọng (Note)
> **Ghi chú:** Toàn bộ câu chuyện, tên, nhân vật và sự cố được mô tả trong dự án này đều là **hư cấu (fictitious)**. Không có ý định nhận dạng hay suy luận với bất kỳ người thực tế nào. Dữ liệu được chia sẻ đã được tạo ra cho **mục đích sư phạm (pedagogical purposes)**.

---

### Cấu Trúc Dữ Liệu Chi Tiết (Column Descriptions)
* **Nguồn:** Dữ liệu lịch sử chuyến đi của **TLC New York City**.
* **Kích thước:** Tập dữ liệu chứa **22,699 dòng** (mỗi dòng là một chuyến đi) và **18 cột**.

| Tên Cột | Mô Tả |
| :--- | :--- |
| **ID** | Mã số định danh chuyến đi. |
| **VendorID** | Mã nhà cung cấp TPEP: **1**= Creative Mobile Technologies, LLC; **2**= VeriFone Inc. |
| **tpep_pickup_datetime** | Ngày và giờ đồng hồ được bật (bắt đầu chuyến đi). |
| **tpep_dropoff_datetime** | Ngày và giờ đồng hồ được tắt (kết thúc chuyến đi). |
| **Passenger_count** | Số lượng hành khách trong xe. **Đây là giá trị do tài xế nhập.** |
| **Trip_distance** | Khoảng cách chuyến đi đã đi (theo **dặm/miles**), được báo cáo bởi đồng hồ tính cước. |
| **PULocationID** | Mã Khu vực Taxi TLC (TLC Taxi Zone) nơi đồng hồ được bật (**bắt đầu** chuyến đi). |
| **DOLocationID** | Mã Khu vực Taxi TLC nơi đồng hồ được tắt (**kết thúc** chuyến đi). |
| **RateCodeID** | Mã cước phí cuối cùng có hiệu lực khi chuyến đi kết thúc: **1**= Standard rate; **2**=JFK; **3**=Newark; **4**=Nassau or Westchester; **5**=Negotiated fare; **6**=Group ride. |
| **Store_and_fwd_flag** | Cờ báo hiệu chuyến đi được lưu tạm thời trên bộ nhớ xe trước khi gửi đến nhà cung cấp (Y= store and forward trip; N= not a store and forward trip). |
| **Payment_type** | Mã số hình thức hành khách đã thanh toán: **1**= Credit card; **2**= Cash; **3**= No charge; **4**= Dispute; **5**= Unknown; **6**= Voided trip. |
| **Fare_amount** | **Tiền cước phí tính theo thời gian và khoảng cách** được tính bởi đồng hồ tính cước. |
| **Extra** | Phụ phí linh tinh. Hiện tại, chỉ bao gồm phụ phí giờ cao điểm ($0.50) và qua đêm ($1). |
| **MTA_tax** | Thuế MTA $0.50 (tự động kích hoạt dựa trên mức cước đang sử dụng). |
| **Improvement_surcharge** | Phụ phí cải tiến $0.30 (đánh giá khi bật đồng hồ. Bắt đầu thu từ năm 2015). |
| **Tip_amount** | Tiền boa. Trường này **tự động điền cho tiền boa bằng thẻ tín dụng**. **Tiền boa tiền mặt không được bao gồm.** |
| **Tolls_amount** | Tổng số tiền cầu đường đã trả trong chuyến đi. |
| **Total_amount** | Tổng số tiền hành khách phải trả. **Không bao gồm tiền boa tiền mặt.** |

## Công Nghệ và Quy Trình Thực Hiện

### Công Nghệ
* **Ngôn ngữ:** Python (phiên bản 3.12)
* **Thư viện:** Pandas, NumPy.
* **Môi trường:** Visual Studio Code.

### Quy Trình Xử Lý Dữ Liệu (Methodology Steps)
1.  **Tải và Khám phá:** Tải dữ liệu, kiểm tra nhanh cấu trúc, kiểu dữ liệu, và các giá trị bị thiếu/trùng lặp.
2.  **Làm sạch Dữ liệu:** Xử lý các giá trị ngoại lai (outliers) trong các cột `fare_amount` và `trip_distance`.
3.  **Kỹ thuật Tính năng (Feature Engineering):** Tạo ra các biến mới quan trọng, ví dụ như:
    * **Thời gian Chuyến đi:** Tính toán `trip_duration`.
    * **Thời điểm:** Chiết xuất `day_of_week`, `hour`, `month` từ thời gian.
4.  **Phân tích Thống kê:** Thực hiện phân tích mối quan hệ giữa các biến mới và biến mục tiêu (`fare_amount`).

## 💡 Tóm Tắt Kết Quả Chính và Phát Hiện (Executive Summary Highlights)

### Tình Trạng Dự Án Hoàn Thành (Project Status)
Giai đoạn tiền xử lý dữ liệu đã hoàn thành, xây dựng nền tảng vững chắc cho mô hình hóa:

* **Khám phá Dữ liệu:** Đã thực hiện kiểm tra sơ bộ để tìm kiếm và xác định các **giá trị bất thường (unusual values)**.
* **Xác định Biến Chính:** Đã xem xét và chọn ra các biến hữu ích nhất cho mô hình dự đoán, cụ thể là **`total_amount`** và **`trip_distance`** vì chúng mô tả trực tiếp chuyến đi taxi.
* **Nền tảng Tương lai:** Đã xây dựng cơ sở dữ liệu sạch và sẵn sàng cho các bước **phân tích dữ liệu khám phá (EDA)**, trực quan hóa và xây dựng mô hình hồi quy (regression model) trong tương lai.

### Thông Tin Chi Tiết Chính (Key Insights)

Phân tích ban đầu đã mang lại những hiểu biết quan trọng:

1.  **Tính hữu dụng của Dữ liệu:** Bộ dữ liệu bao gồm các biến số rất hữu ích và phù hợp cho việc xây dựng mô hình dự đoán giá cước taxi.
2.  **Giá trị Ngoại Lai Quan trọng:** Đã xác định được các trường hợp **giá trị bất thường** đáng chú ý, cụ thể là **những chuyến đi có quãng đường rất ngắn hoặc bằng 0 (`trip_distance`) nhưng lại có chi phí tổng cộng (`total_amount`) hoặc cước phí cơ bản (`fare_amount`) rất cao**. Điều này đòi hỏi các bước làm sạch và xử lý dữ liệu chi tiết hơn.

| trip\_distance | fare\_amount |
| :---: | :---: |
| 2.60 | 999.99 |
| 0.00 | 450.00 |
| 33.92 | 200.01 |
| 0.00 | 175.00 |
| 0.00 | 200.00 |
| 32.72 | 107.00 |
| 25.50 | 140.00 |
| 7.30 | 152.00 |
| 0.00 | 120.00 |
| 33.96 | 150.00 |

## Liên Hệ

Dự án được thực hiện bởi [@TriNet-IT](https://github.com/TriNet-IT)

* **GitHub:** [@TriNet-IT](https://github.com/TriNet-IT)
* **Email:** ngphtri15@gmail.com
  

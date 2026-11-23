# Mega Sale Lương Về — TikTok Shop (Landing Page)

Trang web chiến dịch tĩnh **Mega Sale Lương Về** của TikTok Shop, xây dựng bằng
HTML + CSS + JavaScript thuần (khung framework, không backend), sẵn sàng đẩy
lên GitHub và triển khai trên **Render Static Site**.

## Cấu trúc thư mục

```text
mega-sale-luong-ve/
├── index.html              # Trang duy nhất của chiến dịch
├── css/
│   └── styles.css          # Toàn bộ style + responsive desktop/mobile
├── js/
│   ├── config.js           # CẤU HÌNH: 2 URL cổng đăng ký (chỉnh ở đây)
│   └── main.js             # Menu mobile + đồng bộ link đăng ký
├── assets/
│   ├── logo-mega-sale-luong-ve.png      # Logo chiến dịch
│   ├── logo-tiktok-shop-white.png       # Logo chính thức TikTok Shop (navbar)
│   ├── bg-racing-desktop.png            # Background đường đua (desktop)
│   ├── bg-racing-mobile.png             # Background đường đua (mobile)
│   ├── heading-dac-quyen-thuong.png     # Tiêu đề "Đặc quyền thưởng"
│   ├── reward-cards-desktop.png         # 3 thẻ thưởng (ngang, desktop)
│   └── reward-cards-mobile.png          # 3 thẻ thưởng (dọc, mobile)
└── README.md
```

## 1. Chạy thử trên máy local

Không cần build. Chọn một trong hai cách:

- **Cách nhanh nhất:** mở trực tiếp file `index.html` bằng trình duyệt.
- **Chạy bằng local server (khuyến nghị):**

  ```bash
  cd mega-sale-luong-ve
  python3 -m http.server 8080
  ```

  Sau đó truy cập <http://localhost:8080>. Dừng server bằng `Ctrl + C`.

## 2. Cập nhật 2 URL đăng ký ở đâu?

Hai link đăng ký chính thức nằm trong **khu vực cấu hình được đánh dấu rõ ràng**:

1. **`js/config.js`** → object `REGISTRATION_URLS` (`GATE_1`, `GATE_2`). Đây là
   nguồn cấu hình tập trung, JavaScript sẽ tự đồng bộ vào 2 nút khi trang tải.
2. **`index.html`** → tìm comment `CẤU HÌNH URL ĐĂNG KÝ`, sửa thuộc tính
   `href` của 2 thẻ `#gate-1` và `#gate-2`. Bước này giúp link vẫn hoạt động
   ngay cả khi JavaScript chưa chạy.

Nhớ cập nhật **cả hai nơi** với cùng một URL. Không rút gọn hay thay link bằng
URL không chính thức. Mỗi nút luôn mở trong tab mới
(`target="_blank"` + `rel="noopener noreferrer"`).

## 3. Đẩy code lên GitHub

```bash
# 1. Tạo repository mới trên GitHub (qua giao diện web), ví dụ: mega-sale-luong-ve
# 2. Tại thư mục gốc dự án:
cd mega-sale-luong-ve
git init
git add .
git commit -m "Initial commit: Mega Sale Lương Về landing page"
git branch -M main
git remote add origin https://github.com/<USERNAME>/<REPO_NAME>.git
git push -u origin main
```

## 4. Triển khai trên Render (Static Site)

1. Đăng nhập Render → **New +** → **Static Site** → kết nối repository GitHub
   `mega-sale-luong-ve`.
2. Cấu hình:
   - **Language / Framework:** Static Site (không cần chọn framework).
   - **Build Command:** **để trống** — site thuần tĩnh, không có bước build.
   - **Publish Directory:** `.` (chính thư mục gốc chứa `index.html`).
3. Giữ nguyên các thiết lập mặc định khác → **Create Static Site**.
4. Render sẽ cấp một URL public; mỗi lần `git push` nhánh `main`, site tự động
   deploy lại.

## Ghi chú kỹ thuật

- Responsive theo hai điểm rơi chính: tablet (≤ 900px) và mobile (≤ 768px).
  Mobile dùng background dọc riêng và bộ thẻ thưởng xếp dọc riêng.
- Điều hướng cuộn mịn tới các section: Trang chủ · Đăng ký · Đặc quyền thưởng ·
  Thể lệ; menu mobile có nút đóng/mở và tự đóng khi chọn mục.
- Semantic HTML, `aria-label`, trạng thái focus rõ ràng, hỗ trợ
  `prefers-reduced-motion`, không có thanh cuộn ngang.
- Không có form, ô tìm kiếm, bộ đếm giả hay nội dung ngoài thông tin chiến dịch.

/* ==========================================================================
   CẤU HÌNH CHIẾN DỊCH — KHU VỰC CHỈNH SỬA DUY NHẤT
   --------------------------------------------------------------------------
   Khi cần đổi link đăng ký, hãy sửa URL ở CẢ HAI nơi để đồng bộ:
     1. File này (REGISTRATION_URLS bên dưới) — nguồn cấu hình tập trung.
     2. Thuộc tính href của 2 nút trong index.html (tìm "CẤU HÌNH URL
        ĐĂNG KÝ"). Cập nhật href giúp link vẫn hoạt động ngay cả khi
        JavaScript chưa tải xong.
   Không rút gọn hay thay thế bằng link khác ngoài link chính thức.
   ========================================================================== */

window.CAMPAIGN_CONFIG = {
  REGISTRATION_URLS: {
    // Cổng đăng ký 1
    GATE_1: "https://m.tiktok.shop/s/ALwOPFFNfQsc",
    // Cổng đăng ký 2
    GATE_2: "https://m.tiktok.shop/s/ALwOMifNfG1Q",
  },
};

# -*- coding: utf-8 -*-
import os

svg_path = r"C:\Users\PC\Downloads\mu_linh\ban_ve_ky_thuat_mu_linh_spartan.svg"
html_path = r"C:\Users\PC\Downloads\mu_linh\ban_ve_kich_thuoc_mu_linh.html"

# 1. Tạo file SVG Bản vẽ kỹ thuật Vector chất lượng cao
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 2300" width="100%" height="100%" style="background:#0b1120; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="smallGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="0.8"/>
    </pattern>
    <pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse">
      <rect width="100" height="100" fill="url(#smallGrid)"/>
      <path d="M 100 0 L 0 0 0 100" fill="none" stroke="#334155" stroke-width="1.5"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#ff9500" />
    </marker>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#1992b0" />
    </marker>
  </defs>

  <!-- Lưới nền Blueprint -->
  <rect width="100%" height="100%" fill="#0b1120" />
  <rect width="100%" height="100%" fill="url(#grid)" opacity="0.65" />

  <!-- Khung tiêu đề Header -->
  <g id="title-block" transform="translate(50, 40)">
    <rect width="1500" height="105" rx="8" fill="#1e293b" stroke="#1992b0" stroke-width="2.5" />
    <text x="30" y="44" fill="#1992b0" font-size="28" font-weight="900" letter-spacing="1.5">BẢN VẼ KỸ THUẬT &amp; KÍCH THƯỚC MŨ CHIẾN BINH SPARTA (KING LEONIDAS 300)</text>
    <text x="30" y="78" fill="#94a3b8" font-size="16">Tiêu chuẩn khuôn đầu người Việt Nam (55 - 57 cm, Size M/L) | Tỷ lệ bản vẽ: 1 cm = 20 px | Vật liệu: Bìa carton sóng 3 lớp</text>
    <rect x="1230" y="20" width="240" height="66" rx="6" fill="#0b1120" stroke="#ff9500" stroke-width="2" />
    <text x="1350" y="45" fill="#ff9500" font-size="13" font-weight="bold" text-anchor="middle">CHU VI LÒNG NÓN</text>
    <text x="1350" y="70" fill="#f8fafc" font-size="20" font-weight="900" text-anchor="middle">58.5 - 59.0 cm</text>
  </g>

  <!-- 1. NỬA VÒM CHÓP NÓN (DOME HALF) -->
  <g id="part1-dome" transform="translate(60, 185)">
    <rect width="710" height="40" rx="4" fill="#1992b0" opacity="0.25" />
    <text x="15" y="27" fill="#38bdf8" font-size="18" font-weight="bold">1. NỬA VÒM CHÓP NÓN (DOME HALF) - CẮT 2 MẢNH (ĐỐI XỨNG)</text>
    <text x="15" y="62" fill="#94a3b8" font-size="13">Uốn cong và khép 3 khe xẻ (Darts) lại để tạo thành bán cầu elip 3D ôm khít sọ đầu.</text>

    <!-- Hình vẽ biên dạng nửa chỏm cầu -->
    <path d="M 50 430 
             Q 345 450 640 430 
             L 640 280
             Q 610 200 540 180
             L 525 330
             L 510 180
             Q 440 150 365 140
             L 345 390
             L 325 145
             Q 220 170 150 205
             L 135 365
             L 120 220
             Q 70 270 50 430 Z" 
          fill="rgba(25, 146, 176, 0.18)" stroke="#38bdf8" stroke-width="3" stroke-linejoin="round" />

    <!-- Đường đứt nét biểu thị đường khép khe xẻ -->
    <line x1="128" y1="365" x2="128" y2="435" stroke="#ff9500" stroke-width="1.8" stroke-dasharray="5,4" />
    <line x1="345" y1="390" x2="345" y2="445" stroke="#ff9500" stroke-width="1.8" stroke-dasharray="5,4" />
    <line x1="518" y1="330" x2="518" y2="435" stroke="#ff9500" stroke-width="1.8" stroke-dasharray="5,4" />

    <!-- Chú thích khe xẻ Darts -->
    <text x="128" y="395" fill="#fb923c" font-size="12" font-weight="bold" text-anchor="middle">Xẻ 1.8cm</text>
    <text x="345" y="420" fill="#fb923c" font-size="12" font-weight="bold" text-anchor="middle">Xẻ 2.7cm</text>
    <text x="518" y="360" fill="#fb923c" font-size="12" font-weight="bold" text-anchor="middle">Xẻ 1.5cm</text>

    <text x="75" y="410" fill="#f8fafc" font-weight="bold" font-size="13">Sau gáy</text>
    <text x="580" y="410" fill="#f8fafc" font-weight="bold" font-size="13">Trước trán</text>
    <text x="345" y="240" fill="#38bdf8" font-weight="bold" font-size="15" text-anchor="middle">ĐỈNH ĐẦU (VERTEX)</text>

    <!-- Đường kích thước đáy -->
    <line x1="50" y1="465" x2="640" y2="465" stroke="#ff9500" stroke-width="1.8" marker-start="url(#arrow)" marker-end="url(#arrow)" />
    <text x="345" y="490" fill="#ff9500" font-size="15" font-weight="bold" text-anchor="middle">Độ dài đường chân viền: 29.5 cm (Nửa chu vi nón)</text>

    <!-- Đường kích thước chiều cao vòm -->
    <line x1="665" y1="140" x2="665" y2="430" stroke="#1992b0" stroke-width="1.8" marker-start="url(#arrowBlue)" marker-end="url(#arrowBlue)" />
    <text x="685" y="295" fill="#38bdf8" font-size="14" font-weight="bold" transform="rotate(90, 685, 295)" text-anchor="middle">Chiều cao vòm: 14.5 cm</text>
  </g>

  <!-- 2. MẶT NẠ GIÁP TRƯỚC (FACE PLATE) -->
  <g id="part2-face" transform="translate(830, 185)">
    <rect width="710" height="40" rx="4" fill="#ff9500" opacity="0.25" />
    <text x="15" y="27" fill="#fb923c" font-size="18" font-weight="bold">2. MẶT NẠ GIÁP TRƯỚC (FACE PLATE) - CẮT 2 MẢNH GHÉP ĐỐI XỨNG</text>
    <text x="15" y="62" fill="#94a3b8" font-size="13">Sống mũi chữ T dài 12.5 cm, hốc mắt xếch 18° và 2 cánh má vát nhọn dài 26.5 cm.</text>

    <!-- Biên dạng nửa mặt nạ -->
    <path d="M 120 140 
             Q 230 135 340 128 
             L 330 235
             L 360 275
             L 295 480
             L 210 425
             L 175 360
             L 155 365
             L 120 390
             L 120 140 Z" 
          fill="rgba(255, 149, 0, 0.18)" stroke="#fb923c" stroke-width="3" stroke-linejoin="round" />

    <!-- Hốc mắt xếch -->
    <polygon points="160,225 270,192 270,242 160,272" fill="#0b1120" stroke="#f8fafc" stroke-width="2.5" />
    <text x="215" y="240" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">HỐC MẮT (6.5 x 2.8 cm)</text>

    <!-- Đường giữa sống mũi -->
    <line x1="120" y1="115" x2="120" y2="420" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="6,4" />
    <text x="108" y="270" fill="#38bdf8" font-size="13" font-weight="bold" transform="rotate(-90, 108, 270)" text-anchor="middle">ĐƯỜNG GIỮA SỐNG MŨI (TRỤC ĐỐI XỨNG)</text>

    <!-- Kích thước cao tổng mặt nạ: 26.5 cm -->
    <line x1="65" y1="128" x2="65" y2="480" stroke="#ff9500" stroke-width="1.8" marker-start="url(#arrow)" marker-end="url(#arrow)" />
    <text x="45" y="310" fill="#ff9500" font-size="14" font-weight="bold" transform="rotate(-90, 45, 310)" text-anchor="middle">Chiều cao tổng mặt nạ: 26.5 cm</text>

    <!-- Kích thước sống mũi -->
    <line x1="140" y1="140" x2="140" y2="390" stroke="#1992b0" stroke-width="1.8" marker-start="url(#arrowBlue)" marker-end="url(#arrowBlue)" />
    <text x="150" y="330" fill="#38bdf8" font-size="13" font-weight="bold">Sống mũi: 12.5 cm</text>

    <!-- Kích thước nửa trán -->
    <line x1="120" y1="105" x2="340" y2="105" stroke="#ff9500" stroke-width="1.8" marker-start="url(#arrow)" marker-end="url(#arrow)" />
    <text x="230" y="95" fill="#ff9500" font-size="13" font-weight="bold" text-anchor="middle">Rộng nửa trán: 15.5 cm (Toàn trán 31 cm)</text>

    <text x="300" y="505" fill="#fb923c" font-size="13" font-weight="bold">Chóp má nhọn Spartan</text>
  </g>

  <!-- 3. VÀNH LOE SAU GÁY (REAR NECK FLARE) -->
  <g id="part3-neck" transform="translate(60, 725)">
    <rect width="710" height="40" rx="4" fill="#10b981" opacity="0.25" />
    <text x="15" y="27" fill="#34d399" font-size="18" font-weight="bold">3. VÀNH LOE CHE SAU GÁY (REAR NECK FLARE) - CẮT 1 MẢNH</text>
    <text x="15" y="62" fill="#94a3b8" font-size="13">Dải cong hình bán nguyệt dán viền chân sau chỏm cầu tạo độ xòe loe bảo vệ gáy cổ.</text>

    <path d="M 90 230 
             C 210 140, 490 140, 610 230 
             C 470 190, 230 190, 90 230 Z" 
          fill="rgba(16, 185, 129, 0.2)" stroke="#34d399" stroke-width="3" stroke-linejoin="round" />

    <text x="350" y="195" fill="#34d399" font-size="16" font-weight="bold" text-anchor="middle">VÀNH CỔ LOE SAU GÁY</text>
    <text x="350" y="220" fill="#94a3b8" font-size="13" text-anchor="middle">Bản rộng vành: 4.5 cm | Chiều dài cung uốn theo chân nón: 29.0 cm</text>

    <!-- Đường kích thước -->
    <line x1="90" y1="260" x2="610" y2="260" stroke="#ff9500" stroke-width="1.8" marker-start="url(#arrow)" marker-end="url(#arrow)" />
    <text x="350" y="285" fill="#ff9500" font-size="14" font-weight="bold" text-anchor="middle">Chiều dài sải cung: 29.0 cm</text>
  </g>

  <!-- 4. KHUNG MÀO BỜM NGỰA (CREST PLUME BOX) -->
  <g id="part4-crest" transform="translate(830, 725)">
    <rect width="710" height="40" rx="4" fill="#ec4899" opacity="0.25" />
    <text x="15" y="27" fill="#f472b6" font-size="18" font-weight="bold">4. KHUNG MÀO BỜM NGỰA (CREST PLUME BOX) - CẮT 2 MẢNH THÀNH BÊN</text>
    <text x="15" y="62" fill="#94a3b8" font-size="13">Uốn cong theo sống đỉnh nón từ trán ra gáy. Ghép với 3 đệm vuông tạo khe rộng 3.5 cm.</text>

    <path d="M 60 235 
             Q 350 115 640 245 
             L 630 185
             Q 350 55 70 165 
             Z" 
          fill="rgba(236, 72, 153, 0.2)" stroke="#f472b6" stroke-width="3" stroke-linejoin="round" />

    <text x="350" y="135" fill="#f472b6" font-size="15" font-weight="bold" text-anchor="middle">THÀNH MÀO NÓN (CẮT 2 MẢNH)</text>
    <text x="350" y="160" fill="#94a3b8" font-size="12" text-anchor="middle">Đáy cong uốn khít sống lưng vòm nón</text>

    <!-- 3 Miếng đệm (Spacers) -->
    <g transform="translate(220, 270)">
      <rect width="70" height="75" rx="3" fill="#1e293b" stroke="#ff9500" stroke-width="1.8" />
      <text x="35" y="42" fill="#ff9500" font-size="12" font-weight="bold" text-anchor="middle">ĐỆM TRƯỚC</text>
      <text x="35" y="62" fill="#94a3b8" font-size="11" text-anchor="middle">3.5 x 4 cm</text>
    </g>
    <g transform="translate(320, 270)">
      <rect width="70" height="75" rx="3" fill="#1e293b" stroke="#ff9500" stroke-width="1.8" />
      <text x="35" y="42" fill="#ff9500" font-size="12" font-weight="bold" text-anchor="middle">ĐỆM GIỮA</text>
      <text x="35" y="62" fill="#94a3b8" font-size="11" text-anchor="middle">3.5 x 4 cm</text>
    </g>
    <g transform="translate(420, 270)">
      <rect width="70" height="75" rx="3" fill="#1e293b" stroke="#ff9500" stroke-width="1.8" />
      <text x="35" y="42" fill="#ff9500" font-size="12" font-weight="bold" text-anchor="middle">ĐỆM SAU</text>
      <text x="35" y="62" fill="#94a3b8" font-size="11" text-anchor="middle">3.5 x 4 cm</text>
    </g>

    <!-- Kích thước mào -->
    <line x1="60" y1="260" x2="640" y2="260" stroke="#ff9500" stroke-width="1.8" marker-start="url(#arrow)" marker-end="url(#arrow)" />
    <text x="140" y="285" fill="#ff9500" font-size="13" font-weight="bold">Chiều dài cung đáy: 34.5 cm</text>

    <line x1="350" y1="80" x2="350" y2="155" stroke="#1992b0" stroke-width="1.8" marker-start="url(#arrowBlue)" marker-end="url(#arrowBlue)" />
    <text x="360" y="115" fill="#38bdf8" font-size="12" font-weight="bold">Cao 6.0 cm</text>
  </g>

  <!-- 5. QUY TRÌNH THI CÔNG & NHÂN TRẮC HỌC -->
  <g id="part5-details" transform="translate(60, 1160)">
    <rect width="1480" height="1060" rx="8" fill="#1e293b" stroke="#334155" stroke-width="2" />
    
    <rect x="25" y="25" width="1430" height="46" rx="4" fill="#0b1120" />
    <text x="45" y="55" fill="#38bdf8" font-size="21" font-weight="bold">HƯỚNG DẪN 6 BƯỚC THI CÔNG CHI TIẾT THEO VIDEO CHUẨN XÁC 100%</text>

    <!-- 6 Khối bước -->
    <!-- Bước 1 -->
    <g transform="translate(45, 95)">
      <rect width="440" height="280" rx="6" fill="#0b1120" stroke="#1992b0" stroke-width="1.8" />
      <circle cx="35" cy="35" r="18" fill="#1992b0" />
      <text x="35" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">1</text>
      <text x="70" y="42" fill="#38bdf8" font-size="16" font-weight="bold">VẼ &amp; CẮT BÌA CARTON</text>
      <text x="20" y=\"85\" fill="#e2e8f0" font-size="14">• Dùng thước thẳng &amp; ê-ke vẽ các mảnh theo kích thước.</text>
      <text x="20" y="115" fill="#e2e8f0" font-size="14">• Số lượng chi tiết cần chuẩn bị:</text>
      <text x="35" y="145" fill="#94a3b8" font-size="13">+ Vòm chóp sọ: 2 mảnh (Trái &amp; Phải đối xứng)</text>
      <text x="35" y="175" fill="#94a3b8" font-size="13">+ Mặt nạ giáp trước: 2 mảnh (Ghép sống mũi)</text>
      <text x="35" y="205" fill="#94a3b8" font-size="13">+ Viền má 3D: Cắt thêm 2 mảnh má dán đè tạo gờ dày</text>
      <text x="35" y="235" fill="#94a3b8" font-size="13">+ Vành loe gáy (1 mảnh) &amp; Khung mào (2 mảnh + 3 đệm)</text>
    </g>

    <!-- Bước 2 -->
    <g transform="translate(520, 95)">
      <rect width="440" height="280" rx="6" fill="#0b1120" stroke="#ff9500" stroke-width="1.8" />
      <circle cx="35" cy="35" r="18" fill="#ff9500" />
      <text x="35" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">2</text>
      <text x="70" y="42" fill="#fb923c" font-size="16" font-weight="bold">TẠO HÌNH VÒM SỌ 3D</text>
      <text x="20" y="85" fill="#e2e8f0" font-size="14">• Dùng tay miết uốn cong nhẹ từng sóng carton.</text>
      <text x="20" y="115" fill="#e2e8f0" font-size="14">• Khép 3 khe xẻ (Darts) trên mỗi nửa mảnh vòm.</text>
      <text x="20" y="145" fill="#e2e8f0" font-size="14">• Dán cố định mép ngoài bằng băng dính giấy.</text>
      <text x="20" y="175" fill="#e2e8f0" font-size="14">• Dùng súng bắn keo nến bơm đẫm rãnh mặt trong.</text>
      <text x="20" y="205" fill="#e2e8f0" font-size="14">• Ghép 2 nửa vòm trái/phải dọc theo sống giữa đỉnh.</text>
      <text x="20" y="240" fill="#38bdf8" font-size="13" font-weight="bold">➔ Kết quả: Tạo thành quả cầu vòm ôm khít sọ đầu.</text>
    </g>

    <!-- Bước 3 -->
    <g transform="translate(995, 95)">
      <rect width="440" height="280" rx="6" fill="#0b1120" stroke="#10b981" stroke-width="1.8" />
      <circle cx="35" cy="35" r="18" fill="#10b981" />
      <text x="35" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">3</text>
      <text x="70" y="42" fill="#34d399" font-size="16" font-weight="bold">RÁP MẶT NẠ &amp; VÀNH GÁY</text>
      <text x="20" y="85" fill="#e2e8f0" font-size="14">• Bẻ gập sống mũi dọc đường đối xứng tạo góc V ~110°.</text>
      <text x="20" y="115" fill="#e2e8f0" font-size="14">• Bắn keo nến mép trán vào viền trước của chóp vòm.</text>
      <text x="20" y="145" fill="#e2e8f0" font-size="14">• Uốn 2 cánh má cong nhẹ ôm theo 2 bên quai hàm.</text>
      <text x="20" y="175" fill="#e2e8f0" font-size="14">• Dán thêm lớp viền má thứ 2 đè lên để tạo gờ 3D nổi bật.</text>
      <text x="20" y="205" fill="#e2e8f0" font-size="14">• Dán dải vành loe sau gáy dọc theo chân sau vòm nón.</text>
      <text x="20" y="240" fill="#34d399" font-size="13" font-weight="bold">➔ Kết quả: Bộ khung mũ đã hoàn chỉnh phom dáng!</text>
    </g>

    <!-- Bước 4 -->
    <g transform="translate(45, 405)">
      <rect width="440" height="280" rx="6" fill="#0b1120" stroke="#ec4899" stroke-width="1.8" />
      <circle cx="35" cy="35" r="18" fill="#ec4899" />
      <text x="35" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">4</text>
      <text x="70" y="42" fill="#f472b6" font-size="16" font-weight="bold">LẮP MÀO &amp; CẮM BỜM LÔNG</text>
      <text x="20" y="85" fill="#e2e8f0" font-size="14">• Ghép 2 thành mào với 3 miếng đệm thành khe rãnh U.</text>
      <text x="20" y="115" fill="#e2e8f0" font-size="14">• Bắn keo nến cố định khung mào lên đỉnh sống nón.</text>
      <text x="20" y="145" fill="#e2e8f0" font-size="14">• Chuẩn bị chổi cước nhựa đỏ (broom):</text>
      <text x="35" y="175" fill="#94a3b8" font-size="13">+ Cắt từng túm sợi cước dài khoảng 10 - 12 cm.</text>
      <text x="35" y="205" fill="#94a3b8" font-size="13">+ Nhét và bơm đầy keo nến vào khe rãnh mào.</text>
      <text x="20" y="240" fill="#f472b6" font-size="13" font-weight="bold">➔ Bờm lông chiến binh dựng đứng hùng dũng.</text>
    </g>

    <!-- Bước 5 -->
    <g transform="translate(520, 405)">
      <rect width="440" height="280" rx="6" fill="#0b1120" stroke="#8b5cf6" stroke-width="1.8" />
      <circle cx="35" cy="35" r="18" fill="#8b5cf6" />
      <text x="35" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">5</text>
      <text x="70" y="42" fill="#a78bfa" font-size="16" font-weight="bold">BỒI GIẤY BÁO KEO SỮA (PVA)</text>
      <text x="20" y="85" fill="#e2e8f0" font-size="14">• Pha keo sữa PVA với nước theo tỉ lệ 2 keo : 1 nước.</text>
      <text x="20" y="115" fill="#e2e8f0" font-size="14">• Xé nhỏ giấy báo thành từng mẩu 3x5 cm.</text>
      <text x="20" y="145" fill="#e2e8f0" font-size="14">• Quét keo và dán phủ 1-2 lớp kín toàn bộ bề mặt mũ.</text>
      <text x="20" y="175" fill="#e2e8f0" font-size="14">• Tác dụng: Xóa sạch vân sóng carton, lấp kín các khe nứt,</text>
      <text x="20" y="205" fill="#e2e8f0" font-size="14">  tạo bề mặt đanh cứng như kim loại đúc nguyên khối.</text>
      <text x="20" y="240" fill="#a78bfa" font-size="13" font-weight="bold">➔ Phơi khô tự nhiên 4-6 tiếng (hoặc sấy tóc).</text>
    </g>

    <!-- Bước 6 -->
    <g transform="translate(995, 405)">
      <rect width="440" height="280" rx="6" fill="#0b1120" stroke="#f59e0b" stroke-width="1.8" />
      <circle cx="35" cy="35" r="18" fill="#f59e0b" />
      <text x="35" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">6</text>
      <text x="70" y="42" fill="#fbbf24" font-size="16" font-weight="bold">SƠN HIỆU ỨNG ĐỒNG CỔ (300)</text>
      <text x="20" y="85" fill="#e2e8f0" font-size="14">• Dùng mũi dao khía vài vết chém chiến trận (battle scars).</text>
      <text x="20" y="115" fill="#e2e8f0" font-size="14">• Sơn xịt đen nhám (Matte Black) phủ kín mũ &amp; bờm.</text>
      <text x="20" y="145" fill="#e2e8f0" font-size="14">• Kỹ thuật quét cọ khô (Dry-brushing):</text>
      <text x="35" y="175" fill="#94a3b8" font-size="13">+ Chấm cọ vào sơn Acrylic Vàng Đồng (Antique Gold).</text>
      <text x="35" y="205" fill="#94a3b8" font-size="13">+ Quét bớt lên giẻ lau cho đầu cọ gần như khô ráo.</text>
      <text x="35" y="235" fill="#fbbf24" font-size="13" font-weight="bold">➔ Phớt nhẹ lên gờ nổi tạo ánh đồng cổ tuyệt đẹp!</text>
    </g>

    <!-- Bảng thông số nhân trắc học -->
    <g transform="translate(45, 715)">
      <rect width="1390" height="305" rx="6" fill="#0b1120" stroke="#38bdf8" stroke-width="1.8" />
      <text x="30" y="38" fill="#38bdf8" font-size="17" font-weight="bold">BẢNG KÍCH THƯỚC NHÂN TRẮC &amp; ĐỘ HỞ DUNG SAI CHO NGƯỜI VIỆT NAM</text>

      <rect x="30" y="55" width="1330" height="38" fill="#1e293b" />
      <text x="50" y="80" fill="#ff9500" font-size="14" font-weight="bold">BỘ PHẬN</text>
      <text x="280" y="80" fill="#ff9500" font-size="14" font-weight="bold">ĐẦU THỰC TẾ</text>
      <text x="500" y="80" fill="#ff9500" font-size="14" font-weight="bold">LÒNG NÓN CẦN ĐẠT</text>
      <text x="780" y="80" fill="#ff9500" font-size="14" font-weight="bold">KÍCH THƯỚC BẢN VẼ BÌA</text>
      <text x="1100" y="80" fill="#ff9500" font-size="14" font-weight="bold">Ý NGHĨA KỸ THUẬT</text>

      <line x1="30" y1="135" x2="1360" y2="135" stroke="#334155" stroke-width="1" />
      <text x="50" y="120" fill="#f8fafc" font-size="14">Chu vi vòng đầu</text>
      <text x="280" y="120" fill="#94a3b8" font-size="14">55.0 - 57.0 cm (Size M/L)</text>
      <text x="500" y="120" fill="#38bdf8" font-size="14" font-weight="bold">58.5 - 59.0 cm (+2.5 cm)</text>
      <text x="780" y="120" fill="#fbbf24" font-size="14">Nửa vòm: 29.5 cm (x 2 mảnh)</text>
      <text x="1100" y="120" fill="#e2e8f0" font-size="13">Trừ hao bìa carton + lót mút xốp êm</text>

      <line x1="30" y1="180" x2="1360" y2="180" stroke="#334155" stroke-width="1" />
      <text x="50" y="165" fill="#f8fafc" font-size="14">Chiều dài trước - sau</text>
      <text x="280" y="165" fill="#94a3b8" font-size="14">18.5 - 19.2 cm (Trán ra gáy)</text>
      <text x="500" y="165" fill="#38bdf8" font-size="14" font-weight="bold">20.5 - 21.0 cm (+2.0 cm)</text>
      <text x="780" y="165" fill="#fbbf24" font-size="14">Đường cong đỉnh sọ: 34.5 cm</text>
      <text x="1100" y="165" fill="#e2e8f0" font-size="13">Đầu người Việt tròn, tránh kẹp trán/gáy</text>

      <line x1="30" y1="225" x2="1360" y2="225" stroke="#334155" stroke-width="1" />
      <text x="50" y="210" fill="#f8fafc" font-size="14">Chiều rộng ngang đầu</text>
      <text x="280" y="210" fill="#94a3b8" font-size="14">15.2 - 15.8 cm (Thái dương / tai)</text>
      <text x="500" y="210" fill="#38bdf8" font-size="14" font-weight="bold">17.2 - 17.8 cm (+2.0 cm)</text>
      <text x="780" y="210" fill="#fbbf24" font-size="14">Tự mở rộng khi uốn bán cầu</text>
      <text x="1100" y="210" fill="#e2e8f0" font-size="13">Không bị bóp chặt 2 bên thái dương</text>

      <line x1="30" y1="270" x2="1360" y2="270" stroke="#334155" stroke-width="1" />
      <text x="50" y="255" fill="#f8fafc" font-size="14">Chiều cao nón &amp; Mặt nạ</text>
      <text x="280" y="255" fill="#94a3b8" font-size="14">Mắt lên đỉnh: ~12 cm</text>
      <text x="500" y="255" fill="#38bdf8" font-size="14" font-weight="bold">Vòm cao: 14.5 cm | Mặt: 26.5 cm</text>
      <text x="780" y="255" fill="#fbbf24" font-size="14">Sống mũi: 12.5 cm | Mắt: 6.5x2.8 cm</text>
      <text x="1100" y="255" fill="#e2e8f0" font-size="13">Hốc mắt vừa đúng tầm nhìn người lớn</text>
    </g>
  </g>
</svg>"""

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"SVG written to {svg_path}")

# 2. Tạo file HTML Interactive Cẩm nang Bản vẽ Kỹ thuật + Hướng dẫn thi công
html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CẨM NANG BẢN VẼ KỸ THUẬT &amp; KÍCH THƯỚC MŨ CHIẾN BINH SPARTA (300)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Phudu:wght@700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1992b0;
      --accent: #ff9500;
      --bg: #0b1120;
      --card-bg: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Be Vietnam Pro', sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 24px 16px;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    header {{
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      border: 2px solid var(--primary);
      border-radius: 12px;
      padding: 32px 24px;
      margin-bottom: 28px;
      box-shadow: 0 10px 25px -5px rgba(25, 146, 176, 0.2);
    }}
    h1 {{
      font-family: 'Phudu', sans-serif;
      font-size: 30px;
      font-weight: 900;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 12px;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 16px;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      margin-top: 12px;
      background-color: rgba(255, 149, 0, 0.15);
      color: var(--accent);
      border: 1px solid var(--accent);
    }}
    .card {{
      background-color: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 24px;
    }}
    h2 {{
      font-family: 'Phudu', sans-serif;
      font-size: 22px;
      font-weight: 800;
      color: var(--accent);
      text-transform: uppercase;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .svg-container {{
      background-color: #0b1120;
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 16px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      font-size: 14px;
    }}
    th, td {{
      padding: 12px 14px;
      text-align: left;
      border-bottom: 1px solid var(--border);
    }}
    th {{
      background-color: #0f172a;
      color: var(--primary);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 12px;
      letter-spacing: 0.5px;
    }}
    tr:hover td {{
      background-color: rgba(255, 255, 255, 0.02);
    }}
    .highlight {{
      color: var(--accent);
      font-weight: 700;
    }}
    .steps-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-top: 16px;
    }}
    .step-card {{
      background: #0f172a;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 20px;
      position: relative;
    }}
    .step-num {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background-color: var(--primary);
      color: #fff;
      font-weight: 900;
      font-size: 15px;
      margin-bottom: 12px;
    }}
    .step-title {{
      font-size: 17px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 10px;
    }}
    ul.check-list {{
      list-style: none;
    }}
    ul.check-list li {{
      position: relative;
      padding-left: 22px;
      margin-bottom: 8px;
      font-size: 14px;
      color: #cbd5e1;
    }}
    ul.check-list li::before {{
      content: "✔";
      position: absolute;
      left: 0;
      color: var(--primary);
      font-weight: bold;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background-color: var(--primary);
      color: #fff;
      padding: 10px 20px;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 700;
      font-size: 14px;
      border: none;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn:hover {{
      background-color: #157993;
    }}
    .btn-accent {{
      background-color: var(--accent);
    }}
    .btn-accent:hover {{
      background-color: #e08300;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>CẨM NANG BẢN VẼ KỸ THUẬT &amp; KÍCH THƯỚC MŨ CHIẾN BINH SPARTA (300)</h1>
      <p class="subtitle">Bản vẽ thiết kế chuẩn hóa theo nhân trắc học khuôn đầu người Việt Nam (Chu vi 55 - 57 cm, Size M/L) từ video hướng dẫn kênh Channel-[D]-original</p>
      <span class="badge">VẬT LIỆU: BÌA CARTON 3 LỚP + SÚNG BẮN KEO + KEO SỮA PVA + CHỔI CƯỚC ĐỎ</span>
      <div style="margin-top: 16px; display: flex; gap: 12px;">
        <button class="btn btn-accent" onclick="window.print()">🖨️ In bản vẽ kỹ thuật</button>
        <a class="btn" href="ban_ve_ky_thuat_mu_linh_spartan.svg" target="_blank">🔍 Mở file SVG phóng to 100%</a>
      </div>
    </header>

    <!-- SECTION 1: BẢN VẼ TRỰC QUAN -->
    <div class="card">
      <h2>1. BẢN VẼ KỸ THUẬT VECTOR TOÀN DIỆN (INTERACTIVE BLUEPRINT)</h2>
      <p style="color: var(--text-muted); font-size: 14px; margin-bottom: 16px;">
        Bản vẽ gồm đầy đủ 4 chi tiết cấu tạo chính, các đường kích thước đo đạc chuẩn milimet/centimet, các góc vát và hướng dẫn cách vẽ trực tiếp lên bìa carton bằng thước thẳng ê-ke.
      </p>
      <div class="svg-container">
        {svg_content}
      </div>
    </div>

    <!-- SECTION 2: BẢNG THÔNG SỐ ĐO ĐẠC -->
    <div class="card">
      <h2>2. BẢNG THÔNG SỐ NHÂN TRẮC &amp; DUNG SAI CHẾ TẠO</h2>
      <p style="color: var(--text-muted); font-size: 14px;">
        So sánh giữa số đo nhân trắc đầu người Việt Nam và kích thước cắt bìa thực tế để đảm bảo khi đội không bị đau thái dương, không cấn trán và có đủ khoảng hở dán mút xốp êm ái:
      </p>
      <table>
        <thead>
          <tr>
            <th>Bộ phận đo</th>
            <th>Kích thước đầu thực tế</th>
            <th>Kích thước lòng nón</th>
            <th>Thông số bản vẽ cắt bìa</th>
            <th>Lý giải kỹ thuật</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Chu vi vòng đầu</strong></td>
            <td>55.0 - 57.0 cm (Size M/L)</td>
            <td class="highlight">58.5 - 59.0 cm (+2.5 cm)</td>
            <td>Nửa vòm sọ: 29.5 cm (cắt 2 mảnh)</td>
            <td>Độ dung sai bù trừ cho độ dày bìa sóng 3 lớp (3mm) và lớp mút xốp lót êm 5mm.</td>
          </tr>
          <tr>
            <td><strong>Chiều dài trước - sau</strong></td>
            <td>18.5 - 19.2 cm (Trán ra gáy)</td>
            <td class="highlight">20.5 - 21.0 cm (+2.0 cm)</td>
            <td>Cung đỉnh nón: 34.5 cm</td>
            <td>Đầu người Việt có chỉ số Cephalic Index ~82% (dạng tròn ngắn), cần lòng nón dài 20.5cm để không cấn trán.</td>
          </tr>
          <tr>
            <td><strong>Chiều rộng ngang</strong></td>
            <td>15.2 - 15.8 cm (Thái dương)</td>
            <td class="highlight">17.2 - 17.8 cm (+2.0 cm)</td>
            <td>Tự mở rộng khi khép 3 khe xẻ</td>
            <td>Không bị kẹp chặt vào xương gò má và vành tai khi đội lâu.</td>
          </tr>
          <tr>
            <td><strong>Chiều cao vòm &amp; Mặt nạ</strong></td>
            <td>Từ mắt lên đỉnh: ~12.0 cm</td>
            <td class="highlight">Vòm: 14.5 cm | Mặt: 26.5 cm</td>
            <td>Sống mũi: 12.5 cm | Hốc mắt: 6.5x2.8 cm</td>
            <td>Hốc mắt hình bình hành vát xếch 18° đặt vừa khít tâm đồng tử mắt người lớn.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- SECTION 3: QUY TRÌNH 6 BƯỚC THI CÔNG THEO VIDEO -->
    <div class="card">
      <h2>3. QUY TRÌNH THI CÔNG CHI TIẾT THEO VIDEO (6 BƯỚC THỰC CHIẾN)</h2>
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-num">1</div>
          <div class="step-title">Vẽ &amp; Cắt bìa carton</div>
          <ul class="check-list">
            <li>Dùng thước kẻ và bút chì đo vẽ 4 chi tiết lên bìa carton sóng 3 lớp.</li>
            <li>Cắt 2 mảnh vòm chóp sọ (đối xứng trái / phải).</li>
            <li>Cắt 2 mảnh mặt nạ trước (ghép sống mũi).</li>
            <li>Cắt thêm 2 mảnh viền má để dán đè tạo khối gờ nổi 3D đặc trưng.</li>
            <li>Cắt 1 dải vành gáy và 2 thành mào nón + 3 miếng đệm.</li>
          </ul>
        </div>

        <div class="step-card">
          <div class="step-num">2</div>
          <div class="step-title">Tạo hình vòm sọ 3D</div>
          <ul class="check-list">
            <li>Dùng tay vuốt nhẹ để uốn cong các sóng carton.</li>
            <li>Khép 3 khe xẻ (Darts) trên mỗi nửa vòm nón.</li>
            <li>Dán băng keo giấy cố định mép ngoài.</li>
            <li>Bơm ngập keo nến vào các rãnh mí bên trong để tạo lực liên kết vĩnh viễn.</li>
            <li>Ghép 2 nửa vòm lại dọc theo đường sống giữa đỉnh đầu.</li>
          </ul>
        </div>

        <div class="step-card">
          <div class="step-num">3</div>
          <div class="step-title">Ráp mặt nạ &amp; Vành gáy</div>
          <ul class="check-list">
            <li>Bẻ gập sống mũi dọc đường giữa tạo góc chữ V khoảng 110°.</li>
            <li>Bắn keo nến mép trán vào chân trước của vòm chóp sọ.</li>
            <li>Uốn 2 cánh má cong nhẹ ôm theo hai bên quai hàm.</li>
            <li>Dán lớp viền má thứ 2 đè lên để tạo gờ giáp đồng nổi bật.</li>
            <li>Dán dải vành loe sau gáy dọc theo chân sau vòm nón.</li>
          </ul>
        </div>

        <div class="step-card">
          <div class="step-num">4</div>
          <div class="step-title">Lắp mào &amp; Bờm lông chổi cước</div>
          <ul class="check-list">
            <li>Dán 2 thành mào với 3 miếng đệm tạo thành rãnh chữ U rộng 3.5 cm.</li>
            <li>Bắn keo cố định khung mào chạy dọc sống đỉnh nón từ trán ra gáy.</li>
            <li>Cắt các bó sợi chổi cước đỏ (broom) dài 10 - 12 cm.</li>
            <li>Nhét từng chùm cước vào khe mào và bơm keo nến ngập chân lông.</li>
          </ul>
        </div>

        <div class="step-card">
          <div class="step-num">5</div>
          <div class="step-title">Bồi giấy báo keo sữa (PVA)</div>
          <ul class="check-list">
            <li>Pha keo sữa PVA với nước theo tỉ lệ 2 phần keo : 1 phần nước.</li>
            <li>Xé nhỏ giấy báo cũ thành từng mẩu 3x5 cm (không dùng kéo cắt).</li>
            <li>Quét keo và dán phủ 1-2 lớp kín toàn bộ bề mặt bìa carton.</li>
            <li>Xóa sạch vân sóng carton, lấp kín khe mí, giúp mũ cứng đanh như composit.</li>
            <li>Để khô tự nhiên 4-6 tiếng (hoặc dùng máy sấy tóc).</li>
          </ul>
        </div>

        <div class="step-card">
          <div class="step-num">6</div>
          <div class="step-title">Sơn hiệu ứng đồng cổ 300</div>
          <ul class="check-list">
            <li>Dùng dao trổ khía vài vết xém / sẹo chiến trận (battle scars).</li>
            <li>Sơn xịt đen nhám (Matte Black) phủ kín toàn bộ vỏ mũ và cả bờm lông.</li>
            <li>Kỹ thuật quét cọ khô (Dry-brushing): Chấm cọ vào màu Acrylic Vàng Đồng (Antique Gold / Bronze), quét bớt lên giẻ lau rồi phớt nhẹ qua các gờ nổi.</li>
            <li>Mũ lập tức ánh lên chất kim loại đồng đúc cổ đại cực kỳ uy phong!</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML written to {html_path}")

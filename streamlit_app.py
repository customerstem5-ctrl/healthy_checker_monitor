import streamlit as st  # type: ignore[import-not-found]
import pandas as pd  # type: ignore[import-not-found]
import os
from datetime import date

# ============================================================
# PAGE CONFIGURATION
# ============================================================

# ============================================================
# DATA FILE
# ============================================================

DATA_FILE = "health_data.csv"


def save_health_data(data):
    """
    Simpan rekod kesihatan ke dalam CSV.
    Jika fail belum wujud, fail baru akan dicipta.
    """

    new_data = pd.DataFrame([data])

    if os.path.exists(DATA_FILE):
        old_data = pd.read_csv(DATA_FILE)
        updated_data = pd.concat(
            [old_data, new_data],
            ignore_index=True
        )
    else:
        updated_data = new_data

    updated_data.to_csv(
        DATA_FILE,
        index=False
    )

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .health-card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
    }

    .score {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
    }

    .small-text {
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🌱 Healthy Lifestyle Checker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Pantau gaya hidup, fahami kesihatan anda.</div>',
    unsafe_allow_html=True
)

st.write(
    """
    Aplikasi ini membantu anda membuat semakan ringkas terhadap
    beberapa aspek gaya hidup harian seperti BMI, hidrasi,
    tidur, aktiviti fizikal dan pemakanan.
    """
)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌱 Healthy Lifestyle Checker")

st.sidebar.write(
    """
    Gunakan menu ini untuk mengisi maklumat kesihatan anda.
    """
)

st.sidebar.divider()

st.sidebar.info(
    """
    ⚠️ **Peringatan**

    Aplikasi ini adalah untuk tujuan pendidikan dan pemantauan
    gaya hidup sahaja.

    Ia bukan alat diagnosis perubatan.
    """
)

# ============================================================
# SESSION STATE
# ============================================================

if "checked" not in st.session_state:
    st.session_state.checked = False

# ============================================================
# USER PROFILE
# ============================================================

st.header("👤 1. Maklumat Pengguna")

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input(
        "Nama",
        placeholder="Masukkan nama"
    )

with col2:
    age = st.number_input(
        "Umur",
        min_value=10,
        max_value=100,
        value=22
    )

with col3:
    gender = st.selectbox(
        "Jantina",
        ["Lelaki", "Perempuan"]
    )

# ============================================================
# BODY INFORMATION
# ============================================================

st.header("⚖️ 2. Maklumat Badan")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "Berat badan (kg)",
        min_value=20.0,
        max_value=300.0,
        value=60.0,
        step=0.1
    )

with col2:
    height = st.number_input(
        "Tinggi (cm)",
        min_value=100.0,
        max_value=250.0,
        value=170.0,
        step=0.1
    )

# ============================================================
# LIFESTYLE INFORMATION
# ============================================================

st.header("🌱 3. Gaya Hidup Harian")

col1, col2 = st.columns(2)

with col1:

    water = st.number_input(
        "💧 Air diminum hari ini (liter)",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=0.1
    )

    sleep = st.number_input(
        "😴 Tempoh tidur malam tadi (jam)",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )

with col2:

    activity = st.number_input(
        "🏃 Aktiviti fizikal minggu ini (minit)",
        min_value=0,
        max_value=2000,
        value=150,
        step=10
    )

    fruit_vegetable = st.number_input(
        "🍎 Anggaran hidangan buah & sayur sehari",
        min_value=0,
        max_value=15,
        value=3,
        step=1
    )

# ============================================================
# HEALTH INDICATORS
# ============================================================

st.header("❤️ 4. Bacaan Kesihatan")

st.caption(
    "Bahagian ini adalah pilihan. Masukkan bacaan jika anda mempunyainya."
)

col1, col2, col3 = st.columns(3)

with col1:

    heart_rate = st.number_input(
        "❤️ Denyutan jantung rehat (bpm)",
        min_value=30,
        max_value=220,
        value=72
    )

with col2:

    systolic = st.number_input(
        "🩸 Tekanan darah sistolik",
        min_value=50,
        max_value=250,
        value=120
    )

with col3:

    diastolic = st.number_input(
        "🩸 Tekanan darah diastolik",
        min_value=30,
        max_value=150,
        value=80
    )

# ============================================================
# CHECK BUTTON
# ============================================================

st.divider()

check_button = st.button(
    "🔍 ANALISIS GAYA HIDUP SAYA",
    type="primary",
    use_container_width=True
)

# ============================================================
# MAIN CALCULATION
# ============================================================

if check_button:

    st.session_state.checked = True

    # --------------------------------------------------------
    # BMI
    # --------------------------------------------------------

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    # --------------------------------------------------------
    # BMI CATEGORY
    # --------------------------------------------------------

    if bmi < 18.5:

        bmi_category = "Kurang berat badan"

        bmi_advice = (
            "Pertimbangkan memastikan pengambilan makanan yang "
            "mencukupi dan berkhasiat. Jika berat badan rendah "
            "berterusan atau tidak disengajakan, pertimbangkan "
            "berbincang dengan profesional kesihatan."
        )

    elif bmi < 25:

        bmi_category = "Julat BMI normal"

        bmi_advice = (
            "Teruskan mengamalkan pemakanan seimbang dan aktiviti "
            "fizikal secara berkala."
        )

    elif bmi < 30:

        bmi_category = "Berlebihan berat badan"

        bmi_advice = (
            "Pertimbangkan peningkatan aktiviti fizikal secara "
            "beransur-ansur dan beri perhatian kepada corak "
            "pemakanan. BMI ialah ukuran saringan dan bukan "
            "gambaran lengkap kesihatan seseorang."
        )

    else:

        bmi_category = "Obesiti"

        bmi_advice = (
            "Pertimbangkan berbincang dengan profesional kesihatan "
            "untuk mendapatkan nasihat yang sesuai dengan keadaan "
            "dan matlamat anda."
        )

    # ========================================================
    # SCORE CALCULATION
    # ========================================================

    # --------------------------------------------------------
    # BMI SCORE
    # --------------------------------------------------------

    if 18.5 <= bmi < 25:
        bmi_score = 20
    elif 17 <= bmi < 30:
        bmi_score = 15
    else:
        bmi_score = 10

    # --------------------------------------------------------
    # WATER SCORE
    # --------------------------------------------------------

    if water >= 2:
        water_score = 20
    elif water >= 1.5:
        water_score = 15
    elif water >= 1:
        water_score = 10
    else:
        water_score = 5

    # --------------------------------------------------------
    # SLEEP SCORE
    # --------------------------------------------------------

    if 7 <= sleep <= 9:
        sleep_score = 20
    elif 6 <= sleep < 7 or 9 < sleep <= 10:
        sleep_score = 15
    else:
        sleep_score = 10

    # --------------------------------------------------------
    # ACTIVITY SCORE
    # --------------------------------------------------------

    if activity >= 150:
        activity_score = 20
    elif activity >= 100:
        activity_score = 15
    elif activity >= 50:
        activity_score = 10
    else:
        activity_score = 5

    # --------------------------------------------------------
    # NUTRITION SCORE
    # --------------------------------------------------------

    if fruit_vegetable >= 5:
        nutrition_score = 20
    elif fruit_vegetable >= 3:
        nutrition_score = 15
    elif fruit_vegetable >= 1:
        nutrition_score = 10
    else:
        nutrition_score = 5

    # --------------------------------------------------------
    # TOTAL SCORE
    # --------------------------------------------------------

    # ========================================================
    # SAVE HEALTH RECORD
    # ========================================================

    total_score = (
        bmi_score
        + water_score
        + sleep_score
        + activity_score
        + nutrition_score
    )
    health_record = {
        "Tarikh": str(date.today()),
        "Nama": name if name else "Pengguna",
        "Umur": age,
        "Jantina": gender,
        "Berat_kg": weight,
        "Tinggi_cm": height,
        "BMI": round(bmi, 1),
        "Kategori_BMI": bmi_category,
        "Air_Liter": water,
        "Tidur_Jam": sleep,
        "Aktiviti_Minit": activity,
        "Buah_Sayur_Hidangan": fruit_vegetable,
        "Denyutan_Jantung": heart_rate,
        "Sistolik": systolic,
        "Diastolik": diastolic,
        "Lifestyle_Score": total_score
    }

    save_health_data(health_record)

    # ========================================================
    # RESULTS
    # ========================================================

    st.divider()

    st.header("📊 5. Keputusan Analisis")

    # --------------------------------------------------------
    # SCORE DISPLAY
    # --------------------------------------------------------

    st.subheader("🌱 Lifestyle Score")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown(
            f'<div class="score">{total_score}/100</div>',
            unsafe_allow_html=True
        )

        st.progress(total_score / 100)

    # --------------------------------------------------------
    # SCORE DESCRIPTION
    # --------------------------------------------------------

    if total_score >= 80:

        score_message = (
            "Gaya hidup anda menunjukkan beberapa amalan yang baik. "
            "Teruskan dan kekalkan tabiat positif."
        )

        st.success(score_message)

    elif total_score >= 60:

        score_message = (
            "Gaya hidup anda berada pada tahap sederhana. "
            "Terdapat beberapa aspek yang boleh diperbaiki."
        )

        st.warning(score_message)

    else:

        score_message = (
            "Beberapa aspek gaya hidup memerlukan lebih perhatian. "
            "Fokus kepada perubahan kecil dan konsisten."
        )

        st.warning(score_message)

    # ========================================================
    # BMI RESULT
    # ========================================================

    st.subheader("⚖️ BMI")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "BMI",
            f"{bmi:.1f}"
        )

    with col2:

        st.write("**Kategori:**")
        st.write(bmi_category)

    st.info(f"💡 {bmi_advice}")

    # ========================================================
    # LIFESTYLE SUMMARY
    # ========================================================

    st.subheader("🌱 Ringkasan Gaya Hidup")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "💧 Air",
            f"{water:.1f} L"
        )

    with col2:

        st.metric(
            "😴 Tidur",
            f"{sleep:.1f} jam"
        )

    with col3:

        st.metric(
            "🏃 Aktiviti",
            f"{activity} min"
        )

    with col4:

        st.metric(
            "🍎 Buah & Sayur",
            f"{fruit_vegetable} hidangan"
        )

    # ========================================================
    # PERSONALIZED ADVICE
    # ========================================================

    st.divider()

    st.header("🤖 6. Nasihat Peribadi")

    advice_count = 0

    # --------------------------------------------------------
    # WATER ADVICE
    # --------------------------------------------------------

    if water < 1.5:

        advice_count += 1

        st.warning(
            """
            💧 **Hidrasi perlu diberi perhatian**

            Pengambilan air yang anda masukkan hari ini agak rendah.
            Cuba minum secara berkala sepanjang hari dan bawa botol
            air apabila keluar atau melakukan aktiviti fizikal.
            """
        )

    else:

        st.success(
            "💧 **Hidrasi:** Pengambilan air yang anda masukkan "
            "menunjukkan amalan yang baik. Kekalkan pengambilan "
            "cecair secara berkala."
        )

    # --------------------------------------------------------
    # SLEEP ADVICE
    # --------------------------------------------------------

    if sleep < 7:

        advice_count += 1

        st.warning(
            """
            😴 **Tidur perlu diberi perhatian**

            Tempoh tidur yang anda masukkan adalah kurang daripada
            sasaran umum untuk kebanyakan orang dewasa.

            Cuba tetapkan waktu tidur dan bangun yang konsisten,
            serta kurangkan gangguan sebelum tidur.
            """
        )

    elif sleep > 9:

        advice_count += 1

        st.info(
            """
            😴 **Tempoh tidur**

            Anda memasukkan tempoh tidur yang agak panjang.
            Jika keadaan ini kerap berlaku dan anda masih berasa
            letih atau tidak segar selepas tidur, pertimbangkan
            berbincang dengan profesional kesihatan.
            """
        )

    else:

        st.success(
            "😴 **Tidur:** Tempoh tidur yang anda masukkan berada "
            "dalam julat sasaran umum untuk orang dewasa."
        )

    # --------------------------------------------------------
    # ACTIVITY ADVICE
    # --------------------------------------------------------

    if activity < 150:

        advice_count += 1

        remaining = 150 - activity

        st.warning(
            f"""
            🏃 **Aktiviti fizikal boleh ditingkatkan**

            Anda memasukkan {activity} minit aktiviti fizikal
            minggu ini.

            Sasaran umum yang digunakan aplikasi ialah 150 minit
            aktiviti sederhana seminggu.

            Anda memerlukan kira-kira {remaining} minit lagi untuk
            mencapai sasaran tersebut.

            Tingkatkan aktiviti secara beransur-ansur mengikut
            kemampuan anda.
            """
        )

    else:

        st.success(
            f"""
            🏃 **Aktiviti fizikal:** Anda memasukkan {activity}
            minit aktiviti minggu ini dan telah mencapai sasaran
            umum 150 minit seminggu.
            """
        )

    # --------------------------------------------------------
    # NUTRITION ADVICE
    # --------------------------------------------------------

    if fruit_vegetable < 5:

        advice_count += 1

        st.warning(
            f"""
            🍎 **Pemakanan boleh ditambah baik**

            Anda memasukkan {fruit_vegetable} hidangan buah dan
            sayur sehari.

            Cuba tambah buah atau sayur dalam hidangan utama,
            sarapan atau sebagai snek.
            """
        )

    else:

        st.success(
            """
            🍎 **Pemakanan:** Pengambilan buah dan sayur yang
            anda masukkan menunjukkan amalan yang baik.
            Teruskan variasikan sumber makanan.
            """
        )

    # ========================================================
    # HEART RATE
    # ========================================================

    st.divider()

    st.header("❤️ 7. Bacaan Kesihatan")

    st.write(
        f"**Denyutan jantung rehat:** {heart_rate} bpm"
    )

    st.write(
        f"**Tekanan darah:** {systolic}/{diastolic} mmHg"
    )

    # --------------------------------------------------------
    # HEART RATE MESSAGE
    # --------------------------------------------------------

    if heart_rate < 60:

        st.info(
            """
            ❤️ Denyutan jantung rehat anda yang dimasukkan
            adalah di bawah 60 bpm. Bacaan ini boleh berlaku
            dalam sesetengah individu, termasuk individu yang
            sangat aktif. Konteks individu adalah penting.
            """
        )

    elif heart_rate <= 100:

        st.success(
            """
            ❤️ Denyutan jantung rehat anda yang dimasukkan
            berada dalam julat umum yang sering digunakan
            untuk orang dewasa.
            """
        )

    else:

        st.warning(
            """
            ❤️ Denyutan jantung rehat anda yang dimasukkan
            adalah melebihi julat umum 60–100 bpm yang sering
            digunakan untuk orang dewasa.

            Jika bacaan tinggi berulang atau disertai gejala,
            pertimbangkan mendapatkan penilaian profesional
            kesihatan.
            """
        )

    # --------------------------------------------------------
    # BLOOD PRESSURE MESSAGE
    # --------------------------------------------------------

    if systolic >= 180 or diastolic >= 120:

        st.error(
            """
            🩸 Bacaan tekanan darah yang dimasukkan adalah sangat
            tinggi. Ulang pengukuran dengan teknik yang betul.

            Jika bacaan kekal sangat tinggi, terutama jika terdapat
            gejala seperti sakit dada, sesak nafas, kelemahan,
            perubahan penglihatan atau kesukaran bercakap,
            dapatkan rawatan kecemasan.
            """
        )

    elif systolic >= 130 or diastolic >= 80:

        st.warning(
            """
            🩸 Bacaan tekanan darah yang dimasukkan berada pada
            tahap yang memerlukan perhatian berdasarkan kategori
            tekanan darah dewasa yang biasa digunakan.

            Satu bacaan sahaja tidak mencukupi untuk menentukan
            diagnosis. Pertimbangkan pemantauan dan berbincang
            dengan profesional kesihatan jika bacaan berulang.
            """
        )

    else:

        st.success(
            """
            🩸 Bacaan tekanan darah yang dimasukkan tidak melepasi
            ambang perhatian yang digunakan oleh aplikasi ini.
            """
        )

    # ========================================================
    # FINAL RECOMMENDATION
    # ========================================================

    st.divider()

    st.header("🎯 8. Cadangan Utama")

    if advice_count == 0:

        st.success(
            """
            🌟 **Tahniah!**

            Berdasarkan maklumat yang anda masukkan, kebanyakan
            aspek gaya hidup berada pada keadaan yang baik.

            Fokus sekarang ialah mengekalkan konsistensi.
            """
        )

    else:

        st.write(
            "Berdasarkan data anda, cuba fokus kepada perkara berikut:"
        )

        if water < 1.5:

            st.write(
                "💧 Tingkatkan pengambilan air secara berkala."
            )

        if sleep < 7:

            st.write(
                "😴 Beri lebih perhatian kepada tempoh dan rutin tidur."
            )

        if activity < 150:

            st.write(
                "🏃 Tingkatkan aktiviti fizikal secara beransur-ansur."
            )

        if fruit_vegetable < 5:

            st.write(
                "🍎 Tambahkan buah dan sayur dalam pemakanan harian."
            )

        if bmi >= 25:

            st.write(
                "⚖️ Beri perhatian kepada corak pemakanan, aktiviti "
                "fizikal dan perubahan berat dari masa ke masa."
            )

    # ========================================================
    # REPORT
    # ========================================================

    st.divider()

    st.header("📋 9. Ringkasan Laporan")

    report_name = name if name else "Pengguna"

    st.write(f"**Nama:** {report_name}")
    st.write(f"**Umur:** {age} tahun")
    st.write(f"**Jantina:** {gender}")
    st.write(f"**Tarikh:** {date.today()}")

    st.write("---")

    report_col1, report_col2 = st.columns(2)

    with report_col1:

        st.write(f"⚖️ BMI: **{bmi:.1f}**")
        st.write(f"📌 Kategori BMI: **{bmi_category}**")
        st.write(f"💧 Air: **{water:.1f} L**")
        st.write(f"😴 Tidur: **{sleep:.1f} jam**")

    with report_col2:

        st.write(f"🏃 Aktiviti: **{activity} min/minggu**")
        st.write(
            f"🍎 Buah & sayur: **{fruit_vegetable} hidangan/hari**"
        )
        st.write(f"❤️ Denyutan jantung: **{heart_rate} bpm**")
        st.write(
            f"🩸 Tekanan darah: **{systolic}/{diastolic} mmHg**"
        )

    st.divider()

    st.caption(
        """
        Penafian: Healthy Lifestyle Checker ialah aplikasi
        pendidikan dan pemantauan gaya hidup. Keputusan aplikasi
        tidak boleh digunakan untuk membuat diagnosis atau
        menggantikan nasihat profesional kesihatan.
        """
    )
# ============================================================
# HEALTH HISTORY
# ============================================================

st.divider()

st.header("📈 10. Sejarah Kesihatan")

if os.path.exists(DATA_FILE):

    history = pd.read_csv(DATA_FILE)

    st.subheader("📋 Rekod Kesihatan")

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )

    # ========================================================
    # CHARTS
    # ========================================================

    st.subheader("📊 Perkembangan Kesihatan")

    chart_type = st.selectbox(
        "Pilih data untuk dipaparkan",
        [
            "Lifestyle Score",
            "BMI",
            "Berat",
            "Air",
            "Tidur",
            "Aktiviti"
        ]
    )

    if chart_type == "Lifestyle Score":

        st.line_chart(
            history.set_index("Tarikh")["Lifestyle_Score"]
        )

    elif chart_type == "BMI":

        st.line_chart(
            history.set_index("Tarikh")["BMI"]
        )

    elif chart_type == "Berat":

        st.line_chart(
            history.set_index("Tarikh")["Berat_kg"]
        )

    elif chart_type == "Air":

        st.line_chart(
            history.set_index("Tarikh")["Air_Liter"]
        )

    elif chart_type == "Tidur":

        st.line_chart(
            history.set_index("Tarikh")["Tidur_Jam"]
        )

    elif chart_type == "Aktiviti":

        st.line_chart(
            history.set_index("Tarikh")["Aktiviti_Minit"]
        )

else:

    st.info(
        "📭 Belum ada rekod kesihatan. "
        "Buat analisis pertama anda untuk melihat sejarah."
    )

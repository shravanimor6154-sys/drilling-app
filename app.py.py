import streamlit as st

st.set_page_config(page_title="Drilling System", layout="centered")

st.title("🛢 Intelligent Drilling Decision System")

st.write("Enter drilling parameters to predict pore pressure and safety")

# 🔹 Inputs
depth = st.number_input("Enter Depth (meters)", min_value=0.0)
density = st.number_input("Enter Density", min_value=0.0)

fluid = st.selectbox("Select Fluid Type", ["Water", "Oil", "Gas"])

# 🔹 Button
if st.button("Predict & Analyze"):

    # 🔸 Base pressure calculation
    pressure = depth * density * 0.1

    # 🔸 Modify based on fluid type
    if fluid == "Gas":
        pressure *= 1.2   # gas increases risk
    elif fluid == "Oil":
        pressure *= 1.1

    # 🔸 Risk Classification
    if pressure < 2000:
        risk = "SAFE 🟢"
        safe_depth = depth
    elif pressure < 4000:
        risk = "MODERATE 🟡"
        safe_depth = depth - 100
    else:
        risk = "HIGH RISK 🔴"
        safe_depth = depth - 200

    # 🔹 Output Section
    st.subheader("📊 Results")

    st.write(f"Predicted Pore Pressure: {pressure:.2f} psi")
    st.write(f"Risk Level: {risk}")
    st.write(f"Recommended Safe Depth: {safe_depth:.2f} meters")

    # 🔹 Warning Signals
    st.subheader("⚠️ System Alerts")

    if pressure < 2000:
        st.success("Conditions are safe for drilling.")
    elif pressure < 4000:
        st.warning("Pressure increasing. Proceed with caution.")
    else:
        st.error("🚨 HIGH RISK! Stop drilling immediately!")

    # 🔹 Suggestions
    st.subheader("💡 Recommendations")

    if pressure >= 4000:
        st.write("- Reduce drilling speed")
        st.write("- Increase monitoring")
        st.write("- Adjust drilling mud weight")
    elif pressure >= 2000:
        st.write("- Monitor pressure continuously")
        st.write("- Proceed carefully")
    else:
        st.write("- Safe to continue drilling")
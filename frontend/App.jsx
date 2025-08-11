import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./services/Auth";
import LandingPage from "./pages/landingpage";
import DoctorLogin        from "./pages/Doctorlogin";
import Register           from "./pages/Register";
import DoctorDashboard    from "./pages/doctordash";
import DoctorAppointments from "./pages/DoctorAppointment";
import DoctorPatients     from "./pages/DoctorPatients";
import DoctorSettings     from "./pages/DoctorSettings";
import RoleSelector from "./pages/roleselector";
import PatientLogin from "./pages/patlogin";
import PatientDashboard from "./pages/patientdasboard";
import BookAppointments from "./pages/BookAppointments";
import ChatWithMCP from "./pages/ChatWithMCP";
import AppointmentsPage from "./pages/appointment";
import DoctorsPage from './components/DoctorListpage';
import DoctorChatAgent from "./components/DoctorChatAgent";
import NotFoundPage from "./pages/NotFoundPage";
import MemoryTestChat from "./pages/test";
import PatientChatWithGuide from "./pages/PatientBOOKCHAT.jsx";
import LabsAndPrescriptions from "./pages/labs&pres.jsx";


function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* 1. Root → login */}
          <Route path="/" element={<LandingPage />} />
          <Route path="/select-role" element={<RoleSelector/>}/>
          {/* 2. Public */}
          <Route path="/doctorlogin" element={<DoctorLogin />} />
          <Route path="/register"      element={<Register />} />

          {/* 3. Protected doctor views */}
          <Route path="/doctors"                  element={<DoctorDashboard />} />
          <Route path="/doctors/appointments"     element={<DoctorAppointments />} />
          <Route path="/doctors/patients"         element={<DoctorPatients />} />
          <Route path="/doctors/settings"         element={<DoctorSettings />} />

          {/* 4. Catch‐all → root */}
          <Route path="*" element={<NotFoundPage/>} />

          {/*5 patient */}
          <Route path="patientlogin"           element={<PatientLogin/>} />
          <Route path="patients" element={< PatientDashboard/>}/>
          <Route path="/patients/bookappointments"  element={<BookAppointments />}/>
          <Route path="/patients/lab"  element={<ChatWithMCP />}/>

          <Route path="/appointments" element={<AppointmentsPage />} />
         <Route path="*" element={<Navigate to="/appointments" />} />  
          <Route path="/doctor-chat" element={<DoctorChatAgent />} />
          
          <Route path="/memoryTestChat" element={<MemoryTestChat />} />

          <Route path="patients/pchat" element={< PatientChatWithGuide/>} />
          <Route path="patients/doctors" element={<DoctorsPage />} />
          <Route path="/doctors/labs&prescription" element={<LabsAndPrescriptions />} />
          
          {/* 6. Test */}
        
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;

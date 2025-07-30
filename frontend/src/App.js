import React, { useState, useEffect, useRef } from 'react';
import { User, Phone, Plus, Trash2, Shield, AlertTriangle, Check } from 'lucide-react';

// Auth Components
const LoginPage = ({ onLogin, onSwitchToRegister, loading }) => {
  const [form, setForm] = useState({ email: '', password: '' });

  const handleSubmit = () => {
    if (!form.email || !form.password) {
      alert('Please fill in all fields');
      return;
    }
    onLogin(form.email, form.password);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-red-50 to-orange-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md">
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-red-100 rounded-full mb-4">
            <Shield className="w-8 h-8 text-red-600" />
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">RescueAlert</h1>
          <p className="text-gray-600">Your safety companion</p>
        </div>
        
        <div className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
            <input
              type="email"
              required
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
              value={form.email}
              onChange={(e) => setForm({...form, email: e.target.value})}
              placeholder="Enter your email"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Password</label>
            <input
              type="password"
              required
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
              value={form.password}
              onChange={(e) => setForm({...form, password: e.target.value})}
              placeholder="Enter your password"
            />
          </div>
          
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full bg-red-600 text-white py-3 rounded-lg font-medium hover:bg-red-700 disabled:opacity-50 transition-colors"
          >
            {loading ? 'Signing In...' : 'Sign In'}
          </button>
        </div>
        
        <div className="mt-6 text-center">
          <button
            onClick={onSwitchToRegister}
            className="text-red-600 hover:text-red-700 font-medium"
          >
            Don't have an account? Sign Up
          </button>
        </div>
      </div>
    </div>
  );
};

const RegisterPage = ({ onRegister, onSwitchToLogin, loading }) => {
  const [form, setForm] = useState({ name: '', email: '', password: '', confirmPassword: '' });

  const handleSubmit = () => {
    if (!form.name || !form.email || !form.password || !form.confirmPassword) {
      alert('Please fill in all fields');
      return;
    }
    if (form.password !== form.confirmPassword) {
      alert('Passwords do not match');
      return;
    }
    onRegister(form);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-red-50 to-orange-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md">
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-red-100 rounded-full mb-4">
            <Shield className="w-8 h-8 text-red-600" />
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Join RescueAlert</h1>
          <p className="text-gray-600">Create your safety network</p>
        </div>
        
        <div className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Full Name</label>
            <input
              type="text"
              required
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
              value={form.name}
              onChange={(e) => setForm({...form, name: e.target.value})}
              placeholder="Enter your full name"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
            <input
              type="email"
              required
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
              value={form.email}
              onChange={(e) => setForm({...form, email: e.target.value})}
              placeholder="Enter your email"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Password</label>
            <input
              type="password"
              required
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
              value={form.password}
              onChange={(e) => setForm({...form, password: e.target.value})}
              placeholder="Create a password"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Confirm Password</label>
            <input
              type="password"
              required
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
              value={form.confirmPassword}
              onChange={(e) => setForm({...form, confirmPassword: e.target.value})}
              placeholder="Confirm your password"
            />
          </div>
          
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full bg-red-600 text-white py-3 rounded-lg font-medium hover:bg-red-700 disabled:opacity-50 transition-colors"
          >
            {loading ? 'Creating Account...' : 'Create Account'}
          </button>
        </div>
        
        <div className="mt-6 text-center">
          <button
            onClick={onSwitchToLogin}
            className="text-red-600 hover:text-red-700 font-medium"
          >
            Already have an account? Sign In
          </button>
        </div>
      </div>
    </div>
  );
};

// Dashboard Components
const Header = ({ user, onLogout }) => (
  <header className="bg-white shadow-sm border-b border-gray-200">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between items-center h-16">
        <div className="flex items-center">
          <Shield className="w-8 h-8 text-red-600 mr-3" />
          <h1 className="text-xl font-bold text-gray-900">RescueAlert</h1>
        </div>
        <div className="flex items-center space-x-4">
          <span className="text-gray-700">Welcome, {user?.name}</span>
          <button
            onClick={onLogout}
            className="text-red-600 hover:text-red-700 font-medium"
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  </header>
);

const Sidebar = ({ activeTab, onTabChange }) => (
  <div className="w-64 bg-white shadow-lg">
    <nav className="mt-8">
      <button
        onClick={() => onTabChange('main')}
        className={`w-full flex items-center px-6 py-3 text-left ${
          activeTab === 'main' ? 'bg-red-50 text-red-600 border-r-2 border-red-600' : 'text-gray-700 hover:bg-gray-50'
        }`}
      >
        <Shield className="w-5 h-5 mr-3" />
        Emergency Button
      </button>
      
      <button
        onClick={() => onTabChange('add-contact')}
        className={`w-full flex items-center px-6 py-3 text-left ${
          activeTab === 'add-contact' ? 'bg-red-50 text-red-600 border-r-2 border-red-600' : 'text-gray-700 hover:bg-gray-50'
        }`}
      >
        <Plus className="w-5 h-5 mr-3" />
        Add Contact
      </button>
      
      <button
        onClick={() => onTabChange('manage-contacts')}
        className={`w-full flex items-center px-6 py-3 text-left ${
          activeTab === 'manage-contacts' ? 'bg-red-50 text-red-600 border-r-2 border-red-600' : 'text-gray-700 hover:bg-gray-50'
        }`}
      >
        <User className="w-5 h-5 mr-3" />
        Manage Contacts
      </button>
    </nav>
  </div>
);

const EmergencyButton = ({ contacts, onSendAlert, loading }) => {
  const [isPressed, setIsPressed] = useState(false);
  const [pressProgress, setPressProgress] = useState(0);
  const [alertSent, setAlertSent] = useState(false);
  const progressInterval = useRef(null);

  const startRescuePress = () => {
    setIsPressed(true);
    setPressProgress(0);
    setAlertSent(false);
    
    progressInterval.current = setInterval(() => {
      setPressProgress(prev => {
        if (prev >= 100) {
          clearInterval(progressInterval.current);
          sendRescueAlert();
          return 100;
        }
        return prev + 2;
      });
    }, 100);
  };

  const stopRescuePress = () => {
    setIsPressed(false);
    setPressProgress(0);
    if (progressInterval.current) {
      clearInterval(progressInterval.current);
    }
  };

  const sendRescueAlert = async () => {
    try {
      await onSendAlert();
      setAlertSent(true);
      setTimeout(() => {
        setAlertSent(false);
        setPressProgress(0);
        setIsPressed(false);
      }, 3000);
    } catch (error) {
      alert('Failed to send alert. Please try again.');
      setIsPressed(false);
      setPressProgress(0);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-full">
      <div className="text-center mb-12">
        <h2 className="text-4xl font-bold text-gray-900 mb-4">Emergency Rescue</h2>
        <p className="text-xl text-gray-600 mb-2">Press and hold for 5 seconds to send alert</p>
        <p className="text-sm text-gray-500">Release to cancel</p>
      </div>
      
      {alertSent ? (
        <div className="text-center">
          <div className="inline-flex items-center justify-center w-48 h-48 bg-green-100 rounded-full mb-6">
            <Check className="w-24 h-24 text-green-600" />
          </div>
          <h3 className="text-2xl font-bold text-green-600 mb-2">Alert Sent!</h3>
          <p className="text-gray-600">Your emergency contacts have been notified</p>
        </div>
      ) : (
        <div className="relative">
          <button
            onMouseDown={startRescuePress}
            onMouseUp={stopRescuePress}
            onMouseLeave={stopRescuePress}
            onTouchStart={startRescuePress}
            onTouchEnd={stopRescuePress}
            className={`relative w-48 h-48 rounded-full border-8 transition-all duration-200 ${
              isPressed 
                ? 'bg-red-600 border-red-800 scale-95' 
                : 'bg-red-500 border-red-600 hover:bg-red-600 hover:scale-105'
            } flex items-center justify-center text-white font-bold text-xl shadow-2xl`}
            disabled={loading}
          >
            <div className="text-center">
              <AlertTriangle className="w-12 h-12 mb-2 mx-auto" />
              <div>RESCUE</div>
              {isPressed && (
                <div className="mt-2 text-sm">
                  {Math.ceil((5 - (pressProgress / 20)))}s remaining
                </div>
              )}
            </div>
            
            {isPressed && (
              <svg className="absolute inset-0 w-full h-full -rotate-90" viewBox="0 0 100 100">
                <circle
                  cx="50"
                  cy="50"
                  r="46"
                  fill="none"
                  stroke="rgba(255,255,255,0.3)"
                  strokeWidth="4"
                />
                <circle
                  cx="50"
                  cy="50"
                  r="46"
                  fill="none"
                  stroke="white"
                  strokeWidth="4"
                  strokeLinecap="round"
                  strokeDasharray={`${2 * Math.PI * 46}`}
                  strokeDashoffset={`${2 * Math.PI * 46 * (1 - pressProgress / 100)}`}
                  className="transition-all duration-100"
                />
              </svg>
            )}
          </button>
        </div>
      )}
      
      {contacts.length === 0 && (
        <div className="mt-8 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
          <p className="text-yellow-800">
            <strong>Note:</strong> You haven't added any emergency contacts yet. 
            Add contacts to receive alerts when you use the rescue button.
          </p>
        </div>
      )}
    </div>
  );
};

const AddContactForm = ({ onAddContact, loading }) => {
  const [form, setForm] = useState({ name: '', phone: '', relationship: '' });

  const handleSubmit = () => {
    if (!form.name || !form.phone) {
      alert('Please fill in all required fields');
      return;
    }
    onAddContact(form);
    setForm({ name: '', phone: '', relationship: '' });
  };

  return (
    <div className="max-w-md mx-auto">
      <h2 className="text-3xl font-bold text-gray-900 mb-8">Add Emergency Contact</h2>
      
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Name *</label>
          <input
            type="text"
            required
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
            value={form.name}
            onChange={(e) => setForm({...form, name: e.target.value})}
            placeholder="Contact's full name"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Phone Number *</label>
          <input
            type="tel"
            required
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
            value={form.phone}
            onChange={(e) => setForm({...form, phone: e.target.value})}
            placeholder="+1 (555) 123-4567"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Relationship</label>
          <select
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
            value={form.relationship}
            onChange={(e) => setForm({...form, relationship: e.target.value})}
          >
            <option value="">Select relationship</option>
            <option value="Parent">Parent</option>
            <option value="Sibling">Sibling</option>
            <option value="Spouse">Spouse</option>
            <option value="Child">Child</option>
            <option value="Friend">Friend</option>
            <option value="Colleague">Colleague</option>
            <option value="Other">Other</option>
          </select>
        </div>
        
        <button
          onClick={handleSubmit}
          disabled={loading}
          className="w-full bg-red-600 text-white py-3 rounded-lg font-medium hover:bg-red-700 disabled:opacity-50 transition-colors"
        >
          {loading ? 'Adding Contact...' : 'Add Contact'}
        </button>
      </div>
    </div>
  );
};

const ContactsList = ({ contacts, onRemoveContact, onSwitchToAdd }) => {
  if (contacts.length === 0) {
    return (
      <div>
        <h2 className="text-3xl font-bold text-gray-900 mb-8">Emergency Contacts</h2>
        <div className="text-center py-12">
          <User className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-xl font-medium text-gray-600 mb-2">No contacts added yet</h3>
          <p className="text-gray-500 mb-6">Add your emergency contacts to get started</p>
          <button
            onClick={onSwitchToAdd}
            className="bg-red-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-red-700 transition-colors"
          >
            Add First Contact
          </button>
        </div>
      </div>
    );
  }

  return (
    <div>
      <h2 className="text-3xl font-bold text-gray-900 mb-8">Emergency Contacts</h2>
      <div className="grid gap-4">
        {contacts.map((contact) => (
          <div key={contact.id} className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <div className="flex justify-between items-start">
              <div className="flex items-start space-x-4">
                <div className="bg-red-100 p-3 rounded-full">
                  <User className="w-6 h-6 text-red-600" />
                </div>
                <div>
                  <h3 className="text-lg font-medium text-gray-900">{contact.name}</h3>
                  <div className="flex items-center text-gray-600 mt-1">
                    <Phone className="w-4 h-4 mr-2" />
                    {contact.phone}
                  </div>
                  {contact.relationship && (
                    <p className="text-sm text-gray-500 mt-1">{contact.relationship}</p>
                  )}
                </div>
              </div>
              <button
                onClick={() => onRemoveContact(contact.id)}
                className="text-red-600 hover:text-red-700 p-2"
                title="Remove contact"
              >
                <Trash2 className="w-5 h-5" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// Main App Component
const RescueAlert = () => {
  const [currentView, setCurrentView] = useState('login');
  const [user, setUser] = useState(null);
  const [contacts, setContacts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('main');
  
  // Mock API functions - replace with your actual API endpoints
  const mockLogin = async (email, password) => {
    setLoading(true);
    await new Promise(resolve => setTimeout(resolve, 1000));
    setLoading(false);
    return { id: 1, name: 'John Doe', email };
  };
  
  const mockRegister = async (userData) => {
    setLoading(true);
    await new Promise(resolve => setTimeout(resolve, 1000));
    setLoading(false);
    return { id: 1, name: userData.name, email: userData.email };
  };
  
  const mockAddContact = async (contact) => {
    setLoading(true);
    await new Promise(resolve => setTimeout(resolve, 500));
    setLoading(false);
    return { id: Date.now(), ...contact };
  };
  
  const mockSendAlert = async () => {
    setLoading(true);
    await new Promise(resolve => setTimeout(resolve, 1000));
    setLoading(false);
    return { success: true };
  };

  const handleLogin = async (email, password) => {
    try {
      const userData = await mockLogin(email, password);
      setUser(userData);
      setCurrentView('main');
    } catch (error) {
      alert('Login failed. Please try again.');
    }
  };

  const handleRegister = async (formData) => {
    try {
      const userData = await mockRegister(formData);
      setUser(userData);
      setCurrentView('main');
    } catch (error) {
      alert('Registration failed. Please try again.');
    }
  };

  const handleAddContact = async (contactData) => {
    try {
      const newContact = await mockAddContact(contactData);
      setContacts([...contacts, newContact]);
      alert('Contact added successfully!');
    } catch (error) {
      alert('Failed to add contact. Please try again.');
    }
  };

  const handleRemoveContact = (contactId) => {
    setContacts(contacts.filter(contact => contact.id !== contactId));
  };

  const handleSendAlert = async () => {
    await mockSendAlert();
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentView('login');
    setContacts([]);
    setActiveTab('main');
  };

  // Render login page
  if (currentView === 'login') {
    return (
      <LoginPage
        onLogin={handleLogin}
        onSwitchToRegister={() => setCurrentView('register')}
        loading={loading}
      />
    );
  }

  // Render register page
  if (currentView === 'register') {
    return (
      <RegisterPage
        onRegister={handleRegister}
        onSwitchToLogin={() => setCurrentView('login')}
        loading={loading}
      />
    );
  }

  // Render main dashboard
  return (
    <div className="min-h-screen bg-gradient-to-br from-red-50 to-orange-50">
      <Header user={user} onLogout={handleLogout} />
      
      <div className="flex h-screen">
        <Sidebar activeTab={activeTab} onTabChange={setActiveTab} />
        
        <div className="flex-1 p-8">
          {activeTab === 'main' && (
            <EmergencyButton
              contacts={contacts}
              onSendAlert={handleSendAlert}
              loading={loading}
            />
          )}
          
          {activeTab === 'add-contact' && (
            <AddContactForm
              onAddContact={handleAddContact}
              loading={loading}
            />
          )}
          
          {activeTab === 'manage-contacts' && (
            <ContactsList
              contacts={contacts}
              onRemoveContact={handleRemoveContact}
              onSwitchToAdd={() => setActiveTab('add-contact')}
            />
          )}
        </div>
      </div>
    </div>
  );
};

export default RescueAlert;